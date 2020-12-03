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

document.addEventListener('DOMContentLoaded', function(){

    // Get the modal
    var modal = document.getElementById("myModal");

    // Get the button that opens the modal
    var btn = document.getElementById("myBtn");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks on the button, open the modal
    btn.onclick = function() {
    modal.style.display = "block";
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
    modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
    }
});