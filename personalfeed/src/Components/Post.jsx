import React from "react";

const Post = ({post}) => {

    return (
        <div>
            <p> {post.name} </p>
            <p> {post.message} </p>
            <p> {post.date} </p>
            <p>
                <hr></hr>
            </p>
        </div>
    )
}
export default Post;