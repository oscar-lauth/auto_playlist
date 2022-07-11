from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from SECRETS import CLIENT_ID
import random
import string

router = APIRouter()

@router.get("/login/")
async def auth_user():
    redirect_uri = "http://localhost:8000/callback"
    state = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 16))
    scope = "user-read-private user-read-email"
    q_params = f"client_id={CLIENT_ID}&response_type=code&redirect_uri={redirect_uri}&state={state}&scope={scope}"
    url = f"https://accounts.spotify.com/authorize?{q_params}"
    response = RedirectResponse(url=url)
    return response

@router.get("/callback/")
async def callback(q):
    # return(q)
    pass
