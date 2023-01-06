let scrollbutton = document.getElementById("scrollBtn");

window.onscroll = function() {scrollFunction()};


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