import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import About from './components/About';
import CreatePost from './components/CreatePost';
import FeaturedVideos from './components/FeaturedVideos';
import './styles/TerminalStyle.css';

function App() {
  return (
    <Router>
      <div className="App terminal">
        <Header />
        <Routes>
          <Route path="/" element={<Header />} />
          <Route path="/about" element={<About />} />
          <Route path="/create" element={<CreatePost />} />
          <Route path="/videos" element={<FeaturedVideos />} />
         
        </Routes>
      </div>
    </Router>
  );
}

export default App;