import React from 'react';
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Quiz from './pages/Quiz';
import Login from './pages/Login';
import Generate from './pages/Generate';

let answers:{}[] = [];
function App() {
  return (
     <Router>
       <div className="App">
      <Routes>
        <Route path='/' element={<Login/>}/>
        <Route path='/quiz' element={<Quiz handleQuizDone={(ans)=>{
          answers = ans;
        }}/>}/>
        <Route path='/generate' element={<Generate params={answers}/>}/>
      </Routes>
    </div>
     </Router>
  );
}

export default App;
