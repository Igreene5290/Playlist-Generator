import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import requests


# Permissions for application
scope = "playlist-modify-public user-library-read"

def fetch_artist_info(sp, artist_id):
    """Fetch artist information with retry."""
    return sp.artist(artist_id)

def fetch_all_liked_songs(sp):
    """Fetch all liked songs from the user's Spotify account."""
    liked_songs = []
    results = sp.current_user_saved_tracks()
    while results:
        liked_songs.extend(results['items'])
        if results['next']:
            results = sp.next(results)
        else:
            break
    return liked_songs

def group_songs_by_genre(sp, liked_songs):
    """Group songs by genre."""
    song_genres = {}
    for item in liked_songs:
        track = item['track']
        track_id = track['id']
        artist_id = track['artists'][0]['id']

        # Fetch the artist's genre with retry
        try:
            artist_info = fetch_artist_info(sp, artist_id)
            genres = artist_info['genres']
            song_genres[track_id] = genres[0] if genres else "Unknown"
        except requests.exceptions.RequestException as e:
            print(f"Error fetching artist info for track {track_id}: {e}")
            song_genres[track_id] = "Unknown"

    # Group tracks by genre
    genre_to_tracks = {}
    for track_id, genre in song_genres.items():
        if genre not in genre_to_tracks:
            genre_to_tracks[genre] = []
        genre_to_tracks[genre].append(track_id)
    
    return genre_to_tracks

def create_genre_playlists(sp, genre_to_tracks):
    """Create playlists for each genre and add corresponding songs."""
    user_id = sp.me()['id']
    for genre, tracks in genre_to_tracks.items():
        # Skip playlist creation if there are fewer than 15 tracks
        if len(tracks) < 15:
            print(f"Skipping '{genre}' playlist. Only {len(tracks)} tracks found.")
            continue
        
        playlist_name = f"{genre} Playlist"
        playlist_description = f"A playlist for {genre} genre."

        # Create playlist
        playlist = sp.user_playlist_create(
            user=user_id,
            name=playlist_name,
            public=False,
            description=playlist_description
        )

        playlist_id = playlist['id']

        # Spotify API limits track additions to 100 per request
        chunk_size = 100
        for i in range(0, len(tracks), chunk_size):
            chunk = tracks[i:i + chunk_size]
            try:
                sp.playlist_add_items(playlist_id, chunk)
            except Exception as e:
                print(f"Error adding tracks to playlist {playlist_name}: {e}")
        
        print(f"Playlist '{playlist_name}' created with {len(tracks)} tracks!")


