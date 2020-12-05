import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config
from extract import json_extract

# urn is the spotify track ID.
urn = 'spotify:track:5N5k9nd479b1xpDZ4usjrg'


client_credentials_manager = SpotifyClientCredentials(
    client_id=config.client['id'],
    client_secret=config.client['secret']
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# Getting massive JSON formatted string from spotify.
info = sp.track(urn)

# Extracting the fields we want
names = json_extract(info, 'name')

print(names)

final = [names[0], names[-1]]

artist, songName = final

print(artist)
print(songName)

final2 = artist + " - " + songName + ".mp3"
print(final2)


'''See lines 64 in spotdl/download/downloader.py about removing contributing artist's names if in song title.''' 