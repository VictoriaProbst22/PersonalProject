import React, {useState}from "react";
import NavBar from "./Components/NavBar"
import PostMapper from "./Components/PostMapper"
import CreatePost from "./Components/CreatePost"


function App() {

  const [posts, setPosts] = useState([
    {
      name:"Pierson",
      message: "I like Playstation!",
      id:1,
      date: '1-1-2022'
    },
    {
      name:"Natasha",
      message: "I like Nintendo Switch!",
      id:2,
      date: '1-1-2022'
    },
  ])

  function addNewPost(post){
    let tempPosts = [post, ...posts];
    setPosts(tempPosts);
    console.log(tempPosts);
  }

  return (
    <div>
      <NavBar />
      <CreatePost addNewPostProp={addNewPost} />
      <PostMapper array={posts}/>
    </div>
  );
}

export default App;
