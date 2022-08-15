import React, { useState } from 'react'
import AnswerBtn from './AnswerBtn';

interface QuestionCardProps {
    question:string;
    parameter:string,
    options:{answerText:string,answerValue:string}[];
    handleAnswerClick:(ansVal:string,param:string)=>void;
}


const QuestionCard = ({ question,parameter,options,handleAnswerClick }:QuestionCardProps) => {
    const[selectedIndex,setSelectedIndex] = useState(-1);
  return (
    <div className="question-card">
        <h3 className="question">{question}</h3>
        <div className="answer-section">
            {options.map((ans,index)=>
            <AnswerBtn answerText={ans.answerText} answerValue={ans.answerValue} parameter={parameter} handleAnswerClick={()=>{handleAnswerClick(ans.answerValue,parameter);setSelectedIndex(index)}}
         isClicked={selectedIndex===index} key={index}/>
            )}
        </div>
    </div>
  )
}

export default QuestionCard