$(document).ready(function() {
  if ($("#flashes *").length > 0){

    $("#modalId").modal();
  }
});



$(".navbar-toggler").click(function(event, c){
    //$(event.target).addClass("disabled");
    $("nav").toggleClass("navbar-white");
    $("#icon-toggle").toggleClass("cross-icon");
    //setTimeout(()=>{
    //    $(event.target).removeClass("disabled");
    //},500);
});



function scrollToAnchor(aid){
    var aTag = $("div[name='"+ aid +"']");
    $('html,body').animate({scrollTop: aTag.offset().top},'slow');
}

$("#aprop").click(function() {
   scrollToAnchor('Apropos');
});


//Get the button:
mybutton = document.getElementById("myBtnToTop");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
