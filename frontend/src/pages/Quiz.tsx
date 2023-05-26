import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import QuestionCard from '../components/QuestionCard';
import axios from 'axios'

let answers:{[parameter:string]:string} = {};

const Quiz = () => {
    let navigate = useNavigate();

    const questions = [
        {
            questionText: "Private or public?",
            options: [
                {answerText: "For the whole world to enjoy", answerValue: "true"},
                {answerText: "For my eyes only", answerValue: "false"},

            ],
            parameter: "public",

        },
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
                {answerText: "Anything goes", answerValue: ".1",},
                {answerText: "Pop", answerValue: ".1",},
                {answerText: "Rap", answerValue: ".2",},

            ],
            parameter: "acousticness",

        },
        {
            questionText: "What kind of weather?",
            options: [
                {answerText: "Bright and sunny", answerValue: ".6",},
                {answerText: "Rainy day in", answerValue: ".3",},
                {answerText: "Snowstorm", answerValue: ".2",},

            ],
            parameter: "danceability",

        },



    ]

    const addAnswer = (param:string,ansVal:string)=>{
        answers[param] = ansVal;
    }

    const handleQuizDone = ()=>{
        if(Object.keys(answers).length !== questions.length) {
            alert("Answer all questions");
            return;
        }
        const isPublic  = answers.public;
        delete answers.public;
        const attr = answers;
        axios.post('/playlist/'+playlistName+'?public='+isPublic).then(res=>{
            const playlistID:string = res.data.id;
            axios.post('/playlist/generate/'+playlistID,attr).then(res=>{
                console.log("DONE");
            })
        })
    }

    const[playlistName,setPlaylistName] = useState('');
            

  return (
    <div className="quiz-page">
        <div className="question-card">
            <h3 className="question">What's the name of this playlist?</h3>
            <input className="ans-input-text" type="text" spellCheck="false" placeholder="Playlist Name"
            onChange={(e)=>{
                e.preventDefault();
                setPlaylistName(e.target.value);
            }}/>
        </div>
        {questions.map((q)=>(
            <QuestionCard question={q.questionText} parameter={q.parameter} options={q.options} addAnswer={addAnswer}
            />
        ))}
        <button className="auto-btn" onClick={()=>handleQuizDone()}>Playlist Time</button>
    </div>
  )
}

export default Quiz