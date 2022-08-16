import React from 'react'
import AnswerBtn from './AnswerBtn';

interface QuestionCardProps {
    question:string;
    parameter:string,
    options:{answerText:string,answerValue:string}[];
    addAnswer:(param:string,ansVal:string)=>void;
}


const QuestionCard = ({ question,parameter,options,addAnswer }:QuestionCardProps) => {
    const onSelectAnswer = (event:React.FormEvent<HTMLDivElement>)=>{
        let btn = event.target as HTMLButtonElement;
        addAnswer(btn.name,btn.value);
    }
  return (
    <div className="question-card">
        <h3 className="question">{question}</h3>
        <div className='answer-section' onChange={(e)=>{onSelectAnswer(e)}}>
        {options.map((ans,index)=>
            <AnswerBtn
            answerText={ans.answerText}
            answerValue={ans.answerValue}
            parameter={parameter}
            key={index}/>
            )}
        </div>
    </div>
  )
}

export default QuestionCard