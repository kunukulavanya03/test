from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    username: str
    email: str
    password: str
    class Config:
        orm_mode = True

class UserCreateSchema(BaseModel):
    username: str
    email: str
    password: str

class PostSchema(BaseModel):
    id: int
    title: str
    content: str
    author_id: int
    class Config:
        orm_mode = True

class PostCreateSchema(BaseModel):
    title: str
    content: str
    author_id: int

class CommentSchema(BaseModel):
    id: int
    content: str
    author_id: int
    post_id: int
    class Config:
        orm_mode = True

class CommentCreateSchema(BaseModel):
    content: str
    author_id: int
