import requests
from pydantic import BaseModel
import json



class User(BaseModel):
    id:str | None
    access_token:str | None
    refresh_token:str | None


def init_user(access_token:str,refresh_token:str):

    url = "https://api.spotify.com/v1/me"
    headers = {"Authorization":f"Bearer {access_token}","Content-Type":"application/json"}
    response = requests.get(url,headers=headers)
    res_dict = response.json()

    if("error" in res_dict):
        return {"Error": "User creation failed"}
    global user
    user = User(id=res_dict["id"],access_token=access_token,refresh_token=refresh_token)
    return {"Success": user}


def create_playlist(name:str,description:str="Desc",is_public:bool=False):
    
    is_public = str(is_public).lower()
    url = f"https://api.spotify.com/v1/users/{user.id}/playlists"
    params = {"name":name,"description":description,"public":is_public}
    headers = {"Authorization":f"Bearer {user.access_token}","Content-Type":"application/json"}
    response = requests.post(url,data=json.dumps(params),headers=headers)
    return response.json()










