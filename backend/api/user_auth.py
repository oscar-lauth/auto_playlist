
from fastapi import APIRouter, HTTPException, Depends, Cookie, Request
from fastapi.responses import RedirectResponse
import random
import string
from spotify.api import User
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
    redir_response = RedirectResponse(url=url)
    redir_response.set_cookie(key="stored_state",value=state)
    return redir_response

@router.get("/callback")
async def callback(request: Request,state:str,code:str = None, error:str = None,stored_state:str=Cookie(),settings:config.Settings=Depends(config.get_settings)):
    if error=="access_denied":
        raise HTTPException(status_code=403)
    elif state != stored_state:
        raise HTTPException(status_code=401,detail="state mismatch")
    user:User = req_access_token(code,redirect_uri)
    request.session["user"] = user.json()
    if "error" in user:
        raise HTTPException(status_code=400,detail=user["error"])
    display_name = user.display_name;
    redir_response = RedirectResponse(url=settings.frontend_url+'/quiz')
    redir_response.set_cookie(key="display_name",value=display_name)
    return redir_response
    

# maybe a function to grab user_json from request.session and then convert and return as User model
# this will keep all request passing away from spotify functions


