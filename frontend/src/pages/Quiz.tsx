import React, { useState } from 'react';
import { Outlet,Link,useNavigate } from 'react-router-dom';

const answers:string[] = []
interface QuizProps {
    handleQuizDone:(answers:string[])=>void;
}

const Quiz = ({ handleQuizDone }:QuizProps) => {
    let navigate = useNavigate();
    const questions = [
        {
            questionText: "What the fuck?",
            options: [
                {answerText: "Answer1", answerValue: "Ans1"},
                {answerText: "Answer2", answerValue: "Ans2"},
                {answerText: "Answer3", answerValue: "Ans3"},

            ]

        },
        {
            questionText: "What the hell?",
            options: [
                {answerText: "Answer12", answerValue: "Ans12"},
                {answerText: "Answer22", answerValue: "Ans22"},
                {answerText: "Answer32", answerValue: "Ans32"},

            ]

        },

    ]
    

    const [currentQuestion,setQuestion] = useState(0);

    const handleAnswerClick = (ansVal:string)=>{
        answers.push(ansVal);
        const nextQuestion:number = currentQuestion + 1;
        if(nextQuestion === questions.length) {
            handleQuizDone(answers);
            navigate('../generate');
            return;
        }
        setQuestion(nextQuestion);
        
    }


  return (
    <div className="quiz-page">
        <div className="quiz-container">
            <h3 className="question">{questions[currentQuestion].questionText}</h3>
            <div className="answer-section">
                {questions[currentQuestion].options.map(ans =>(
                    <button className="answer" onClick={()=>{handleAnswerClick(ans.answerValue)}}>{ans.answerText}</button>
                ))}
            </div>
        </div>
    </div>
  )
}

export default Quiz