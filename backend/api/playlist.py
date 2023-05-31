from fastapi import APIRouter, HTTPException, Request
from spotify.api import generate_playlist
from spotify.api import create_playlist
from spotify.utils import get_user_from_session

router = APIRouter()

@router.post("/playlist/generate/{p_id}",status_code=201,description="Add songs")
async def add_songs(request: Request, p_id:str,attributes:dict,size:int=20):
    print(attributes)
    user = get_user_from_session(request)
    if user is None:
        raise HTTPException(status_code=401, detail="User session data not found")
    response = generate_playlist(user,p_id,attributes,size)
    return response

@router.post("/playlist/{name}",status_code=201,description="Creates new playlist by name")
async def new_playlist(request: Request, name:str,public:bool):
    user = get_user_from_session(request)
    if user is None:
        raise HTTPException(status_code=401, detail="User session data not found")
    response = create_playlist(user,name,is_public=public)
    return response


    