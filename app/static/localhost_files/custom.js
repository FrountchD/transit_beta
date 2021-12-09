$(document).ready(function() {
  if ($("#flashes *").length > 0){

    $("#modalId").modal();
  }
});


function scrollToAnchor(aid){
    var aTag = $("div[name='"+ aid +"']");
    $('html,body').animate({scrollTop: aTag.offset().top},'slow');
}

$("#aprop").click(function() {
   scrollToAnchor('Apropos');
});
