from spotify_api.user_data import req_refreshed_access_token
from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
import random
import string
from spotify_api.user_data import req_access_token
from SECRETS import CLIENT_ID

router = APIRouter()

redirect_uri = "http://localhost:8000/callback"

@router.get("/login")
async def login_user():
    # try to find way to move ALL external spotify api calls to outside internal REST API calls
    state = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 16))
    scope = "user-read-private user-read-email playlist-modify-private"
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
    return req_access_token(code,redirect_uri)
    
@router.get("/refresh_token")
async def req_refresh():
    return req_refreshed_access_token()

