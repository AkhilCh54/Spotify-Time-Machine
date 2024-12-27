import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

Date = input("Which Year do you want to travel to? Enter in the format YYYY-MM-DD : ")
billboard_url = f"https://www.billboard.com/charts/hot-100/{Date}/"
response = requests.get(url =billboard_url )
billboard_webpage = response.text

soup = BeautifulSoup(billboard_webpage,"html.parser")
top_100 = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in top_100]
print(song_names)

spotify_client_id = "" #enter your personal spotify client id
spotify_client_secret = "" #enter your personal spotify client secret

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=spotify_client_id,
        client_secret=spotify_client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username="mimir",
    )
)

# user-library-read
results = sp.current_user()
USER_ID = results['id']
# print(USER_ID) you will need user id to create a playlist and add tracks!

uris = [sp.search(title)['tracks']['items'][0]['uri'] for title in song_names]
PLAYLIST_ID = sp.user_playlist_create(user=USER_ID,public=False,name=f"{Date} BillBoard-100")['id']

sp.user_playlist_add_tracks(playlist_id=PLAYLIST_ID,tracks=uris,user=USER_ID)