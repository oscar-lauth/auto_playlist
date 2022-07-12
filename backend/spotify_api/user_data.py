import requests
# import json
import base64
from SECRETS import CLIENT_ID, CLIENT_SECRET, set_authorization,get_authorization, REFRESH_TOKEN


def req_access_token(code:str,redirect_uri:str):
    auth_params = {
        "grant_type":"authorization_code",
        "code":code,
        "redirect_uri":redirect_uri,
    }
    enc_client_tokens = base64.b64encode((CLIENT_ID+":"+CLIENT_SECRET).encode("utf-8"))
    headers = {"Authorization": "Basic "+ enc_client_tokens.decode("ascii"),
    "Content-Type":"application/x-www-form-urlencoded"}
    response = requests.post("https://accounts.spotify.com/api/token",data=auth_params,headers=headers)
    res_dict = response.json()
    if("error" in res_dict):
        return res_dict
    set_authorization(res_dict["access_token"])
    print("ACCESS STORED")
    REFRESH_TOKEN = res_dict["refresh_token"]
    

def req_refreshed_access_token():
    auth_params = {
        "grant_type":"refresh_token",
        "refresh_token":REFRESH_TOKEN,
        "client_id":CLIENT_ID,
    }
    enc_client_tokens = base64.b64encode((CLIENT_ID+":"+CLIENT_SECRET).encode("utf-8"))
    headers = {"Authorization": "Basic "+ enc_client_tokens.decode("ascii"),
    "Content-Type":"application/x-www-form-urlencoded"}
    response = requests.post("https://accounts.spotify.com/api/token",data=auth_params,headers=headers)
    return response.json()


def get_user_id():
    url = "https://api.spotify.com/v1/me"
    headers = {"Authorization":get_authorization(),"Content-Type":"application/json"}
    response = requests.get(url,headers=headers)
    res_dict = response.json()
    print(res_dict)
    if("error" in res_dict):
        return res_dict
    return res_dict["id"]