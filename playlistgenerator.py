import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# Load environment variables
clientID = os.environ.get('CLIENT_ID')
clientSecret = os.environ.get('CLIENT_SECRET')
URI = os.environ.get('URI')

# Test environment variables
print(f"clientID: {clientID}")
# print(f"clientSecret: {clientSecret}")
# print(f"URI: {URI}")

#Permissions for application
scope = "user-library-read playlist-modify-public playlist-modify-private"

oauth = SpotifyOAuth(client_id = clientID, client_secret = clientSecret, redirect_uri = URI, scope = scope)

sp = spotipy.Spotify(auth_manager = oauth)

def quit():
    print("Thank you for using the Spotify Playlist Generator, Goodbye.")
    exit()


def main():
    print("Welcome to the Spotify Playlist Generator\n")
    playlistName = input("Enter a name for your new playlist, or enter 'q' to quit\n")
    if(playlistName == "q"):
        quit()
    else:
        print("Testing liked songs to playlists\n")

        # Add songs to the playlist
        # Liked songs -> playlists
        liked_songs = []
        results = sp.current_user_saved_tracks()
        while results:
            liked_songs.extend(results['items'])
            if results['next']:
                results = sp.next(results)
            else:
                break


        # Step 2: Get Genre Information for Each Song
        for item in liked_songs['items']:
            track = item['track']
            track_id = track['id']
            artist_id = track['artists'][0]['id']
            
            # Fetch the artist's genre
            artist_info = sp.artist(artist_id)
            genres = artist_info['genres']
            
            # If genres are found, map them to the song's genre (use the first genre if multiple)
            song_genres[track_id] = genres[0] if genres else "Unknown"
            
            # You can also fetch audio features to help with classification if genre isn't available
            # audio_features = sp.audio_features(track_id)

        # Step 3: Group Songs by Genre
        genre_to_tracks = {}
        for track_id, genre in song_genres.items():
            if genre not in genre_to_tracks:
                genre_to_tracks[genre] = []
            genre_to_tracks[genre].append(track_id)

        # Step 4: Create Playlists for Each Genre
        user_id = sp.me()['id']
        for genre, tracks in genre_to_tracks.items():
            # Create playlist for the genre
            playlist_name = f"{genre} Playlist"
            playlist_description = f"A playlist for {genre} genre."
            
            playlist = sp.user_playlist_create(
                user=user_id,
                name=playlist_name,
                public=False,  # Set to True if you want it to be public
                description=playlist_description
            )
            
            # Add songs to the playlist
            sp.playlist_add_items(playlist['id'], tracks)
            print(f"Playlist '{playlist_name}' created and songs added!")
        

# Main Program
main() 


