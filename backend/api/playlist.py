from fastapi import APIRouter, Request
from spotify.api import generate_playlist
from spotify.api import create_playlist

router = APIRouter()

@router.post("/playlist/generate/{p_id}",status_code=201,description="Add songs")
async def add_songs(request: Request, p_id:str,attributes:dict,size:int=20):
    print(attributes)
    response = generate_playlist(request,p_id,attributes,size)
    return response

@router.post("/playlist/{name}",status_code=201,description="Creates new playlist by name")
async def new_playlist(request: Request, name:str,public:bool):
    response = create_playlist(request,name,is_public=public)
    return response


    