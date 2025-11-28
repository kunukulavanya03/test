# Community Blog

This is a community-driven blog and mobile app, built using FastAPI and SQLAlchemy.

## Setup

1. Clone the repository
2. Create a new PostgreSQL database
3. Update the `.env` file with your database credentials
4. Run `pip install -r requirements.txt`
5. Run `uvicorn app.main:app --host 0.0.0.0 --port 8000`

## API Endpoints

* `GET /api/v1/posts`: Retrieve a list of all blog posts
* `GET /api/v1/posts/{post_id}`: Retrieve a single blog post by ID
* `POST /api/v1/posts`: Create a new blog post
* `PUT /api/v1/posts/{post_id}`: Update an existing blog post
* `DELETE /api/v1/posts/{post_id}`: Delete a blog post by ID
* `POST /api/v1/posts/{post_id}/comments`: Create a new comment on a blog post
* `GET /api/v1/posts/{post_id}/comments`: Retrieve a list of comments on a blog post
* `POST /api/v1/auth/register`: Register a new user account
* `POST /api/v1/auth/login`: Login to an existing user account
