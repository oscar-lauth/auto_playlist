import React from 'react';
import { useNavigate } from 'react-router-dom';
import QuestionCard from '../components/QuestionCard';
import axios from 'axios'

let answers:{[parameter:string]:string}[] = []
// interface QuizProps {
//     handleQuizDone:(answers:{}[])=>void;
// }

const Quiz = () => {
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
            parameter: "weatha",

        },
        {
            questionText: "Ben?",
            options: [
                {answerText: "Yes", answerValue: "sunny",},
                {answerText: "No", answerValue: "rainy",},
                {answerText: "Ughh", answerValue: "snowy",},

            ],
            parameter: "ben",

        },



    ]

    const handleAnswerClick = (answerValue:string,parameter:string)=>{
        answers.forEach((ans)=>{
            if(ans[parameter]!=undefined && ans[parameter]!=answerValue) {
                ans[parameter]= answerValue;
                return;
            }
        })
        answers.push({[parameter]:answerValue});
        // console.log(answers);
    }

    const handleQuizDone = ()=>{
        console.log(answers);
        if(answers.length!==questions.length) {
            console.log("NO");
            return;
        }
        console.log(answers);
        axios.post('/playlist/Granty').then(res=>{
            const playlist_id : string = res.data.id;
            axios.post('/playlist/generate/'+playlist_id).then(res=>{
            })
          })
        
    }
            

  return (
    <div className="quiz-page">
        {questions.map((q)=>(
            <QuestionCard question={q.questionText} parameter={q.parameter} options={q.options} handleAnswerClick={handleAnswerClick}/>
        ))}
        <button className="auto-btn" onClick={()=>handleQuizDone()}>Playlist Time</button>
    </div>
  )
}

export default Quiz