import React from 'react';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Quiz from './pages/Quiz';
import Login from './pages/Login';

function App() {
  return (
     <Router>
       <div className="App">
      <Routes>
        <Route path='/' element={<Login/>}/>
        <Route path='/quiz' element={<Quiz/>}/>
      </Routes>
    </div>
     </Router>
  );
}

export default App;
