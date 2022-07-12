
import requests
from SECRETS import get_authorization
from spotify_api.user_data import get_user_id
import json


def new_playlist(name:str):
    user_id = get_user_id()
    print(user_id)
    if "error" in user_id:
        return user_id
    url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    params = {"name":name,"description":"FOO","public":"false"}
    headers = {"Authorization":get_authorization(),"Content-Type":"application/json"}
    print("url:"+url)
    print("params:"+str(params))
    print("headers:"+str(headers))
    response = requests.post(url,data=json.dumps(params),headers=headers)
    return response.json()