# from . import api
from .api import init_user
import requests
# import json
import base64
import config
from fastapi import Depends


def req_access_token(code:str,redirect_uri:str,settings:config.Settings=Depends(config.get_settings)):
    auth_params = {
        "grant_type":"authorization_code",
        "code":code,
        "redirect_uri":redirect_uri,
    }
    enc_client_tokens = base64.b64encode((settings.client_id+":"+settings.client_secret).encode("utf-8"))
    headers = {"Authorization": "Basic "+ enc_client_tokens.decode("ascii"),
    "Content-Type":"application/x-www-form-urlencoded"}
    response = requests.post("https://accounts.spotify.com/api/token",data=auth_params,headers=headers)
    res_dict = response.json()
    if("error" in res_dict):
        return res_dict
    return init_user(res_dict["access_token"],res_dict["refresh_token"])
    

# def req_refreshed_access_token():
#     auth_params = {
#         "grant_type":"refresh_token",
#         "refresh_token":REFRESH_TOKEN,
#         "client_id":CLIENT_ID,
#     }
#     enc_client_tokens = base64.b64encode((CLIENT_ID+":"+CLIENT_SECRET).encode("utf-8"))
#     headers = {"Authorization": "Basic "+ enc_client_tokens.decode("ascii"),
#     "Content-Type":"application/x-www-form-urlencoded"}
#     response = requests.post("https://accounts.spotify.com/api/token",data=auth_params,headers=headers)
#     return response.json()