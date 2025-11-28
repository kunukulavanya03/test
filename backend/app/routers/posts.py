from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from app.database import SessionLocal
from app.models import Post
from app.schemas import PostSchema, PostCreateSchema
from app.utils import get_db

router = APIRouter(prefix='/api/v1/posts', tags=['posts'])

@router.get('')
def read_posts(db: SessionLocal = Depends(get_db)):
    posts = db.query(Post).all()
    return JSONResponse(content=[post.__dict__ for post in posts], media_type='application/json')

@router.get('/{post_id}')
def read_post(post_id: int, db: SessionLocal = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        return JSONResponse(content={'error': 'Post not found'}, media_type='application/json', status_code=404)
    return JSONResponse(content=post.__dict__, media_type='application/json')

@router.post('')
def create_post(post: PostCreateSchema, db: SessionLocal = Depends(get_db)):
    new_post = Post(title=post.title, content=post.content, author_id=post.author_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return JSONResponse(content=new_post.__dict__, media_type='application/json', status_code=201)

@router.put('/{post_id}')
def update_post(post_id: int, post: PostCreateSchema, db: SessionLocal = Depends(get_db)):
    existing_post = db.query(Post).filter(Post.id == post_id).first()
    if existing_post is None:
        return JSONResponse(content={'error': 'Post not found'}, media_type='application/json', status_code=404)
    existing_post.title = post.title
    existing_post.content = post.content
    db.commit()
    db.refresh(existing_post)
    return JSONResponse(content=existing_post.__dict__, media_type='application/json')

@router.delete('/{post_id}')
def delete_post(post_id: int, db: SessionLocal = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        return JSONResponse(content={'error': 'Post not found'}, media_type='application/json', status_code=404)
    db.delete(post)
    db.commit()
    return JSONResponse(content={'message': 'Post deleted successfully'}, media_type='application/json')
