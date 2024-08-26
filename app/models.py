from pydantic import BaseModel


class CreatePostIn(BaseModel):
    title:str
    content:str