import React, { useState } from 'react';
import { Outlet,Link,useNavigate } from 'react-router-dom';
import QuestionCard from '../components/QuestionCard';

const answers:{}[] = []
interface QuizProps {
    handleQuizDone:(answers:{}[])=>void;
}

const Quiz = ({ handleQuizDone }:QuizProps) => {
    let navigate = useNavigate();

    // type QuestionItem = {
    //     questionText:string;
    //     options:{
    //         answerText:string;
    //         answerValue:string;
    //         }[];
    //     parameter:string;
    // }

    const questions = [
        {
            questionText: "Popular tunes?",
            options: [
                {answerText: "Tried and trued", answerValue: "90"},
                {answerText: "Somewhere in between", answerValue: "60"},
                {answerText: "Super fresh", answerValue: "10"},

            ],
            parameter: "popularity",

        },
        {
            questionText: "What's the mood?",
            options: [
                {answerText: "Cheerful", answerValue: "1",},
                {answerText: "Neutral", answerValue: ".6",},
                {answerText: "Sad", answerValue: ".2",},

            ],
            parameter: "valence",

        },
        {
            questionText: "Specific genre?",
            options: [
                {answerText: "Anything goes", answerValue: "any",},
                {answerText: "Pop", answerValue: "pop",},
                {answerText: "Rap", answerValue: "rap",},

            ],
            parameter: "genre",

        },
        {
            questionText: "What kind of weather?",
            options: [
                {answerText: "Bright and sunny", answerValue: "sunny",},
                {answerText: "Rainy day in", answerValue: "rainy",},
                {answerText: "Snowstorm", answerValue: "snowy",},

            ],
            parameter: "valence",

        },



    ]

    const [currentQuestion,setQuestion] = useState(0);

    const handleAnswerClick = (ansVal:string,param:string)=>{
        answers.push({[param]:ansVal});
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
        {questions.map((q)=>(
            <QuestionCard question={q.questionText} parameter={q.parameter} options={q.options} handleAnswerClick={handleAnswerClick}/>
        ))}
    </div>
  )
}

export default Quiz