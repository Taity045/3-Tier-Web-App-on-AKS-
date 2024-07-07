import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div className="header">
      <h1 className="prompt">Blog</h1>
      <ul>
        <li><Link to="/about">About</Link></li>
        <li><Link to="/contact">Contact</Link></li>
        <li><Link to="/posts">Posts</Link></li>
        <li><Link to="/videos">Featured Videos</Link></li>
      </ul>
    </div>
  );
}

export default Home;