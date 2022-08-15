import React, { useState } from 'react'

interface AnswerBtnProps {
  answerText:string;
  answerValue:string;
  parameter:string;
  handleAnswerClick:(ansVal:string,param:string)=>void
  isClicked:boolean;
}

const AnswerBtn = ( { answerText, answerValue, parameter, handleAnswerClick, isClicked }:AnswerBtnProps) => {

  return (
        <button className={"answer"+(isClicked ? " is-clicked":"")} onClick={()=>{handleAnswerClick(answerValue,parameter)}}>
            {answerText}
        </button>
  )
}

export default AnswerBtn