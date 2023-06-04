from pydantic import BaseModel

# User model to store important user attributes

class User(BaseModel):

    # Spotify ID of User
    u_id:str | None

    # Spotify display name
    display_name:str | None

    # *internal* User access token
    access_token_:str | None # only to be accessed with init_user, otherwise use .access_token

    # User refresh token
    refresh_token:str | None 

    # time that access token expires in
    expires:int | None # = time at retrieval + seconds till expiration

    # auto refreshes access token when expired
    @property
    def access_token(self)->str:

        # if current time is past expiration time with 60s margin
        # if(time.time() + 60 >= self.expires):

            # request a new access token
            # res_dict = req_refreshed_access_token()

            # set new access token
            # self.access_token_ = res_dict["access_token"]

            # set new expiration time
            # self.expires = res_dict["expires_in"] + int(time.time())

        return self.access_token_