from flask import Flask, request, jsonify, redirect, session
from flask_cors import CORS
import mysql.connector
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import random
import string
from urllib.parse import urlencode
from playlistgenerator import fetch_all_liked_songs, group_songs_by_genre, create_genre_playlists

app = Flask(__name__)
CORS(app)

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="igreene",
    passwd="euclid2015",
    database="playlistgen"
    )

cursor = db.cursor(buffered=True)
cursor.execute("CREATE TABLE IF NOT EXISTS users (humanid int PRIMARY KEY AUTO_INCREMENT, access_token TEXT, refresh_token TEXT, scope VARCHAR(255))")


@app.route('/')
def home():
    return "Welcome to the Playlist Generator API!"

def generateRandomString(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# Load environment variables
clientID = os.environ.get('CLIENT_ID')
clientSecret = os.environ.get('CLIENT_SECRET')
URI = os.environ.get('URI')
scope="playlist-modify-public playlist-modify-private user-read-private user-library-read"
state=generateRandomString(16)


@app.route('/api/spotify-login')
def spotify_login():
    query = urlencode({
        'response_type': 'code',
        'client_id': clientID,
        'scope': scope,
        'redirect_uri': URI,
        'state': state
    })
    return redirect('https://accounts.spotify.com/authorize?' + query)

@app.route('/callback')
def callback():
    # Get the authorization code from Spotify's response
    code = request.args.get('code', None)
    state_received = request.args.get('state', None)

    if not code or not state:
        return jsonify({'error': 'Invalid code or state'}), 400

    token_url = 'https://accounts.spotify.com/api/token'
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': URI,
        'client_id': clientID,
        'client_secret': clientSecret
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(token_url, data=payload, headers=headers)
    token_data = response.json()

    if 'access_token' not in token_data:
        return jsonify({'error': 'Invalid access token'}), 400
    
    
    access_token = token_data['access_token']
    refresh_token = token_data['refresh_token']
    scope = token_data['scope']
    cursor.execute("INSERT INTO users (access_token, refresh_token, scope) VALUES (%s, %s, %s)", (access_token, refresh_token, scope))
    db.commit()

    return redirect("http://localhost:3000/generate")
                    
@app.route('/api/liked-songs-playlists', methods=['POST'])
def liked_songs_playlists():
    cursor.execute("Select humanid FROM users")
    humanids = [row[0] for row in cursor.fetchall()]
    humanid = max(humanids)
    
    
    cursor.execute("SELECT access_token FROM users WHERE humanid = %s", (humanid,))
    result = cursor.fetchone()
    access_token = result[0]

    sp = spotipy.Spotify(auth=access_token)
    print(access_token)
    liked_songs = fetch_all_liked_songs(sp)
    print("liked songs fetched")
    genre_to_tracks = group_songs_by_genre(sp, liked_songs)
    print("genres to tracks")
    create_genre_playlists(sp, genre_to_tracks)
    print("playlists created")

    response = {
        'result': 'success'
    }

    return jsonify(response), 201
    


    

if __name__ == '__main__':
    app.run(debug=True, port=8888)  # Runs on http://127.0.0.1:5000 


    