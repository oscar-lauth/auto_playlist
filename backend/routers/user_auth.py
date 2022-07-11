from SECRETS import CLIENT_SECRET
from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
import requests
from SECRETS import CLIENT_ID
import random
import string
import base64

router = APIRouter()

redirect_uri = "http://localhost:8000/callback"

@router.get("/login")
async def login_user():
    state = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 16))
    scope = "user-read-private user-read-email"
    q_params = f"client_id={CLIENT_ID}&response_type=code&redirect_uri={redirect_uri}&state={state}&scope={scope}"
    url = f"https://accounts.spotify.com/authorize?{q_params}"
    response = RedirectResponse(url=url)
    return response

@router.get("/callback")
async def callback(state:str,code:str = None, error:str = None):
    if error=="access_denied":
        raise HTTPException(status_code=401)
    elif state != state:
        raise HTTPException(status_code=401,detail="state mismatch")
    auth_params = {
        "grant_type":"authorization_code",
        "code":code,
        "redirect_uri":redirect_uri,
    }
    enc_client_tokens = base64.b64encode((CLIENT_ID+":"+CLIENT_SECRET).encode("utf-8"))
    headers = {"Authorization": "Basic "+ enc_client_tokens.decode("ascii"),
    "Content-Type":"application/x-www-form-urlencoded"}
    response = requests.post("https://accounts.spotify.com/api/token",data=auth_params,headers=headers)
    return response.json()
    


