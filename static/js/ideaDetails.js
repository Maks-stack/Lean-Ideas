let commentSection = document.getElementsByClassName("comment-form")[0];
let addCommentButton = document.getElementById("add-comment");


commentSection.style.display = "none";

addCommentButton.addEventListener("click",(event) =>{
    commentSection.style.display = "block";
    addCommentButton.style.display = "none";
});

function goBack(){
    window.history.back();
}