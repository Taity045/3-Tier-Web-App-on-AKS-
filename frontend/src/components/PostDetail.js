import React from 'react';
import { useParams } from 'react-router-dom';

function PostDetail() {
  let { id } = useParams();
  return (
    <div>
      <h1>Post Detail</h1>
      <p>Post ID: {id}</p>
      {/* Add post detail logic here */}
    </div>
  );


}

export default PostDetail;

