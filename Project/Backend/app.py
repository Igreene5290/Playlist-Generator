from flask import Flask, request, jsonify
from flask_cors import CORS
#import spotipy
#from spotipy.oauth2 import SpotifyOAuth
#from playlistgenerator import fetch_all_liked_songs, group_songs_by_genre, create_genre_playlists

app = Flask(__name__)
CORS(app)


@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Flask!"})

if __name__ == '__main__':
    app.run(debug=True)  # Runs on http://127.0.0.1:5000 



##@app.route('/create-playlists', methods=['POST'])
#def create_playlists():
   # """Create playlists for each genre and add corresponding songs."""
    # Fetch all liked songs
   # liked_songs = fetch_all_liked_songs(sp)
    
    # Group songs by genre
   # genre_to_tracks = group_songs_by_genre(sp, liked_songs)
    
    # Create genre playlists
   # create_genre_playlists(sp, genre_to_tracks)
    
  #  return jsonify({"message": "Playlists created successfully!"})

    