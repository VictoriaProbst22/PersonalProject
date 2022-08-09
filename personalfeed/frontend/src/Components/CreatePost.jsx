import React, {useState} from "react";

const CreatePost = (props) => {
    const [name, setName] =useState('')
    const [message, setMessage] =useState('')
    const [date, setDate] =useState('')


    function handleSubmit(event){
        event.preventDefault();
        let newPost ={
            name: name, 
            message: message, 
            date: date,
        };
        console.log(newPost);
        props.addNewPostProp(newPost);

    }

    return ( <form onSubmit={handleSubmit}>
        <div>
            <label> Name </label>
            <input type='text' value={name} onChange={(event)=> setName(event.target.value)} />
        </div>
        <div>
            <lable> Post </lable>
            <input type='text' value={message} onChange={(event)=> setMessage(event.target.value)}/>
        </div>
        <div>
            <lable> Date </lable>
            <input type='date' value={date} onChange={(event)=> setDate(event.target.value)}/>
        </div>
        <div>
            <button type='submit'> Post This! </button>
        </div>

    </form> );
}
 
export default CreatePost;