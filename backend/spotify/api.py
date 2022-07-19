import requests
import time
from pydantic import BaseModel
import json
import config
import base64


# User model to store important user attributes
class User(BaseModel):

    # Spotify ID of User
    u_id:str | None

    # Spotify ID of User's 'auto' playlist
    p_id:str | None

    # *internal* User access token
    access_token_:str | None # only to be accessed with init_user, otherwise use .access_token

    # User refresh token
    refresh_token:str | None 

    # time that access token expires in
    expires:int | None # = time at retrieval + seconds till expiration

    # auto refreshes access token when expired
    @property
    def access_token(self)->str:

        # if current time is past expiration time with 60s margin
        if(time.time() + 60 >= self.expires):

            # request a new access token
            res_dict = req_refreshed_access_token()

            # set new access token
            self.access_token_ = res_dict["access_token"]

            # set new expiration time
            self.expires = res_dict["expires_in"] + int(time.time())

        return self.access_token_

spotify_base_url = "https://api.spotify.com/v1"

# creates new User with passed tokens and profile data from Spotify API
def init_user(access_token:str,refresh_token:str,expires_in:int)->dict:

    expire_time = int(time.time()) + expires_in

    url = spotify_base_url + "/me"
    headers = {"Authorization":f"Bearer {access_token}","Content-Type":"application/json"}
    response = requests.get(url,headers=headers)
    res_dict = response.json()

    if("error" in res_dict):
        return res_dict

     # create User
    global user
    user = User(u_id=res_dict["id"],access_token_=access_token,refresh_token=refresh_token,expires=expire_time)

    return {"Success": "User Authorized"}


# return refreshed access token from Spotify API
def req_refreshed_access_token()->dict:

    # settings from env
    settings:config.Settings = config.get_settings()

    auth_params = {
        "grant_type":"refresh_token",
        "refresh_token":user.refresh_token,
        "client_id":settings.client_id,
    }
    enc_client_tokens = base64.b64encode((settings.client_id+":"+settings.client_secret).encode("utf-8"))
    headers = {"Authorization": "Basic "+ enc_client_tokens.decode("ascii"),
    "Content-Type":"application/x-www-form-urlencoded"}
    response = requests.post("https://accounts.spotify.com/api/token",data=auth_params,headers=headers)
    
    return response.json()


# create an empty playlist for User
def create_playlist(name:str,description:str="Desc",is_public:bool=False)->dict:

    url = spotify_base_url + f"/users/{user.u_id}/playlists"
    params = {"name":name,"description":description,"public":is_public}
    headers = {"Authorization":f"Bearer {user.access_token}","Content-Type":"application/json"}
    response = requests.post(url,data=json.dumps(params),headers=headers)
    res_dict = response.json()
    user.p_id = res_dict["id"]
    return res_dict

# add songs to User's playlist from Spotify song URI's
def add_songs_to_playlist(song_uris:list[str])->dict:
    url = spotify_base_url + f"/playlists/{user.p_id}/tracks"
    params = {"uris":song_uris}
    headers = {"Authorization":f"Bearer {user.access_token}","Content-Type":"application/json"}
    response = requests.post(url,data=json.dumps(params),headers=headers)
    res_dict = response.json()
    return res_dict


def get_recommendations(limit:int=20)->dict:
    url = spotify_base_url + "/recommendations"
    params = build_seed([3,2,0])
    params.update({"limit":limit})
    headers = {"Authorization":f"Bearer {user.access_token}","Content-Type":"application/json"}
    response = requests.get(url,params=params,headers=headers)
    res_dict = response.json()
    return res_dict


def get_top_tracks_raw(limit:int=20,offset:int=0,time_range:str="medium_term")->dict:
    url = spotify_base_url + f"/me/top/tracks"
    params = {"limit":limit,"offset":offset,"time_range":time_range}
    headers = {"Authorization":f"Bearer {user.access_token}","Content-Type":"application/json"}
    response = requests.get(url,params=params,headers=headers)
    res_dict = response.json()
    return res_dict

def get_top_artists_raw(limit:int=20,offset:int=0,time_range:str="medium_term")->dict:
    url = spotify_base_url + f"/me/top/artists"
    params = {"limit":limit,"offset":offset,"time_range":time_range}
    headers = {"Authorization":f"Bearer {user.access_token}","Content-Type":"application/json"}
    response = requests.get(url,params=params,headers=headers)
    res_dict = response.json()
    return res_dict

def get_available_genre_seeds()->list[str]:
    url = spotify_base_url + f"/recommendations/available-genre-seeds"
    headers = {"Authorization":f"Bearer {user.access_token}","Content-Type":"application/json"}
    response = requests.get(url,headers=headers)
    res_dict = response.json()
    return res_dict["genres"]



def get_seed_tracks(top_tracks_raw:dict)->list[str]:
    track_ids:list[str]=[]
    top_tracks = top_tracks_raw["items"]
    for track in top_tracks:
        track_ids.append(track["id"])
    return track_ids


# tracks don't have genres, only artists so this function uses raw top artists to get both artists and genre 
def get_seed_artists_and_genres(top_artists_raw:dict)->dict:
    artist_ids:list[str]=[]
    genres:list[str]=[]
    available_genres = get_available_genre_seeds()
    top_artists = top_artists_raw["items"]
    for artist in top_artists:
        artist_ids.append(artist["id"])
        if(artist["genres"] in available_genres):
            genres.append(artist["genres"])
    return {"artist_ids":artist_ids,"genres":genres}

  
def build_seed(num_values:list[int])->dict:
    if(len(num_values)!=3 or sum(num_values)>5):
        return ["Error, invalid parameters"]
    (n_tracks,n_artists,n_genres) = num_values
    seed_tracks = get_seed_tracks(get_top_tracks_raw())[:n_tracks]
    seed_artists_genres_dict = get_seed_artists_and_genres(get_top_artists_raw())
    seed_artists = seed_artists_genres_dict["artist_ids"][:n_artists]
    seed_genres = seed_artists_genres_dict["genres"][:n_genres]
    return {"seed_tracks":seed_tracks,"seed_artists":seed_artists,"seed_genres":seed_genres}

def generate_playlist(size:int=20):
    song_uris:list[str]=[]
    raw_recs:dict=get_recommendations(size)
    for track in raw_recs["tracks"]:
        song_uris.append(track["uri"])
    return add_songs_to_playlist(song_uris)









