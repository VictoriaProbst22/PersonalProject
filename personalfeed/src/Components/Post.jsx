import React from "react";

const Post = ({post}) => {

    return (
        <div>
            <h2> {post.name} </h2>
            <p> {post.message} </p>
            <p> {post.date} </p>
            <p>
                <hr></hr>
            </p>
        </div>
    )
}
export default Post;