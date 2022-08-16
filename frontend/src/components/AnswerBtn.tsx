import React from 'react'

interface AnswerBtnProps {
  answerText:string;
  answerValue:string;
  parameter:string;
}

const AnswerBtn = ( { answerText, answerValue, parameter, }:AnswerBtnProps) => {

  return (
    <div className="ans-btn">
      <input type="radio"
      id={answerText}
      name={parameter}
      value={answerValue}/>
      <label htmlFor={answerText} className="answer">
        {answerText}
      </label>
    </div>    
  )
}

export default AnswerBtn