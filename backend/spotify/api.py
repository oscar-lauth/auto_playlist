import requests
import time
from pydantic import BaseModel
import json
import config
import base64



class User(BaseModel):

    # Spotify ID of User
    id:str | None

    # User access token
    __access_token:str | None # only to be accessed with init_user, otherwise use .access_token

    # User refresh token
    refresh_token:str | None 

    # time that access token expires in
    expires:int | None # = time at retrieval + seconds till expiration

    @property
    def access_token(self)->str:

        # if current time is past expiration time with 60s margin
        if(time.time() + 60 >= self.expires):

            # request a new access token
            res_dict = req_refreshed_access_token()

            # set new access token
            self.__access_token = res_dict["access_token"]

            # set new expiration time
            self.expires = res_dict["expires_in"] + int(time.time())

        return self.__access_token


def init_user(access_token:str,refresh_token:str,expires_in:int):

    expire_time = int(time.time()) + expires_in

    url = "https://api.spotify.com/v1/me"
    headers = {"Authorization":f"Bearer {access_token}","Content-Type":"application/json"}
    response = requests.get(url,headers=headers)
    res_dict = response.json()

    if("error" in res_dict):
        return {"Error": "User creation failed"}

     # create User
    global user
    user = User(id=res_dict["id"],__access_token=access_token,refresh_token=refresh_token,expires=expire_time)

    return {"Success": user}


def req_refreshed_access_token():

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



def create_playlist(name:str,description:str="Desc",is_public:bool=False):
    
    is_public = str(is_public).lower()
    url = f"https://api.spotify.com/v1/users/{user.id}/playlists"
    params = {"name":name,"description":description,"public":is_public}
    headers = {"Authorization":f"Bearer {user.access_token}","Content-Type":"application/json"}
    response = requests.post(url,data=json.dumps(params),headers=headers)
    
    return response.json()










