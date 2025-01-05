from flask import Flask, request, jsonify, redirect, url_for, redirect
from flask_cors import CORS
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import random
import string
import urllib.parse

app = Flask(__name__)
CORS(app)

def generateRandomString(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# Load environment variables
clientID = os.environ.get('CLIENT_ID')
clientSecret = os.environ.get('CLIENT_SECRET')
URI = os.environ.get('URI')
scope="playlist-modify-public user-library-read"
state=generateRandomString(16)
auth_url = urllib.parse.urlencode({
                        'response_type': 'code',
                        'client_id': clientID,
                        'scope': scope,
                        'redirect_uri': URI,
                        'state': state
                    })


@app.route('/api/spotify-login')
def spotify_login():
    return redirect('https://accounts.spotify.com/authorize?' + auth_url)
                    

if __name__ == '__main__':
    app.run(debug=True)  # Runs on http://127.0.0.1:5000 


    