
from fastapi import APIRouter, HTTPException, Depends, Cookie
from fastapi.responses import RedirectResponse
import random
import string
from spotify.utils import req_access_token
import config

router = APIRouter()

redirect_uri = "http://localhost:8000/callback"

@router.get("/login")
async def login_user(settings:config.Settings=Depends(config.get_settings)):
    # try to find way to move ALL external spotify api calls to outside internal REST API calls
    state = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 16))
    scope = "user-top-read user-read-private user-read-email playlist-modify-private playlist-modify-public"
    q_params = f"client_id={settings.client_id}&response_type=code&redirect_uri={redirect_uri}&state={state}&scope={scope}"
    url = f"https://accounts.spotify.com/authorize?{q_params}"
    red_response = RedirectResponse(url=url)
    red_response.set_cookie(key="stored_state",value=state)
    return red_response

@router.get("/callback")
async def callback(state:str,code:str = None, error:str = None,stored_state:str=Cookie(),settings:config.Settings=Depends(config.get_settings)):
    if error=="access_denied":
        raise HTTPException(status_code=401)
    elif state != stored_state:
        raise HTTPException(status_code=401,detail="state mismatch")
    response = req_access_token(code,redirect_uri)
    if "error" in response:
        raise HTTPException(status_code=400,detail=response["error"])
    display_name = response["display_name"];
    red_response = RedirectResponse(url=settings.frontend_url+'/quiz')
    red_response.set_cookie(key="display_name",value=display_name)
    return red_response
    


