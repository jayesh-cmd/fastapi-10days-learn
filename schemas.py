from pydantic import BaseModel

class TodoCreate(BaseModel):
    task: str
    is_done: bool = False

class TodoResponse(BaseModel):
    id: int
    task: str
    is_done: bool

class usercreate(BaseModel):
    username: str
    password: str

class userlogin(BaseModel):
    username: str
    password: str