import React from 'react';
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Quiz from './pages/Quiz';
import Home from './pages/Home';
import Generate from './pages/Generate';
import Header from './components/Header';
import Footer from './components/Footer';
import Cookies from 'js-cookie';

let answers:{}[] = [];
function App() {
  let displayName = Cookies.get('display_name');
  return (
     <Router>
       <div className="App">
        <Header displayName={displayName}/>
      <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/quiz' element={<Home displayName={displayName}/>}/>
        {/* <Route path='/quiz' element={<Quiz handleQuizDone={(ans)=>{
          answers = ans;
        }}/>}/> */}
        <Route path='/generate' element={<Generate params={answers}/>}/>
      </Routes>
    </div>
     </Router>
  );
}

export default App;
