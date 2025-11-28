# test

blog-website-design---mobile-app-design--Community

## Tech Stack

- **Frontend**: React + Vite
- **Backend**: FastAPI + SQLAlchemy
- **Design**: Figma ([View Design](https://www.figma.com/design/j22YTImTMF2lpL3jyFYkC0/blog-website-design---mobile-app-design--Community-?node-id=0-1&p=f&t=QyZcQIiHiJdlPHqh-0))

## Project Structure

```
test/
├── frontend/          # Frontend application
├── backend/           # Backend API
├── README.md          # This file
└── docker-compose.yml # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Node.js 18+ (for frontend)
- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
```

## Features

- User registration and login
- Blog post creation, editing, and deletion
- Comment creation and retrieval
- User profile management
- Search and filtering of blog posts
- Administrator dashboard for user and post management

## API Endpoints

- `POST /api/v1/auth/register` - Register a new user account.
- `POST /api/v1/auth/login` - Login to an existing user account.
- `GET /api/v1/posts` - Retrieve a list of all blog posts.
- `GET /api/v1/posts/{post_id}` - Retrieve a single blog post by ID.
- `POST /api/v1/posts` - Create a new blog post.
- `PUT /api/v1/posts/{post_id}` - Update an existing blog post.
- `DELETE /api/v1/posts/{post_id}` - Delete a blog post by ID.
- `POST /api/v1/posts/{post_id}/comments` - Create a new comment on a blog post.
- `GET /api/v1/posts/{post_id}/comments` - Retrieve a list of comments on a blog post.

## License

MIT
