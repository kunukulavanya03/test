import React, { useState, useEffect } from 'react';
import axios from 'axios';

export default function Blog() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios.get('/api/v1/posts')
      .then(response => {
        setPosts(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      <h1>Blog</h1>
      <ul>
        {posts.map(post => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  );
}