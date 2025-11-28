from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from app.database import SessionLocal
from app.models import Comment
from app.schemas import CommentSchema, CommentCreateSchema
from app.utils import get_db

router = APIRouter(prefix='/api/v1/posts/{post_id}/comments', tags=['comments'])

@router.post('')
def create_comment(post_id: int, comment: CommentCreateSchema, db: SessionLocal = Depends(get_db)):
    new_comment = Comment(content=comment.content, author_id=comment.author_id, post_id=post_id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return JSONResponse(content=new_comment.__dict__, media_type='application/json', status_code=201)

@router.get('')
def read_comments(post_id: int, db: SessionLocal = Depends(get_db)):
    comments = db.query(Comment).filter(Comment.post_id == post_id).all()
    return JSONResponse(content=[comment.__dict__ for comment in comments], media_type='application/json')
