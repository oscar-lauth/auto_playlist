import React from 'react'

interface QuestionCardProps {
    question:string;
    parameter:string,
    options:{answerText:string,answerValue:string}[];
    handleAnswerClick:(ansVal:string,param:string)=>void;
}

const QuestionCard = ({ question,parameter,options,handleAnswerClick }:QuestionCardProps) => {
  return (
    <div className="question-container">
        <h3 className="question">{question}</h3>
        <div className="answer-section">
            {options.map(ans=>(
                <button className="answer" onClick={()=>handleAnswerClick(ans.answerValue,parameter)}>
                    {ans.answerText}
                </button>
            ))}
        </div>
    </div>
  )
}

export default QuestionCard