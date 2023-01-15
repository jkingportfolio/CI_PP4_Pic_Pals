let scrollbutton = document.getElementById("scrollBtn");

window.onscroll = function() {scrollFunction();};


function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      scrollbutton.style.display = "block";
    } else {
      scrollbutton.style.display = "none";
    }
  }
  
document.getElementById("scrollBtn").addEventListener("click", scrollToTop);

function scrollToTop(event) {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}


// document.getElementById("#id_profile_pic").onclick = function(file_input){
//     const file_input = document.querySelector('#id_profile_pic');
//     file_input.setAttribute('accept', 'image/png, image/jpeg');
// }

// document.getElementById("#id_image").onclick = function(file_input){
//   const file_input = document.querySelector('#id_image');
//   file_input.setAttribute('accept', 'image/png, image/jpeg');
// }