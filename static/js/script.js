$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.carousel').carousel({indicators: true});
    $('select').formSelect();
    $('.modal').modal();
  });

  var btn = $('#button');

$(window).scroll(function() {
  if ($(window).scrollTop() > 300) {
    btn.addClass('show');
  } else {
    btn.removeClass('show');
  }
});

btn.on('click', function(e) {
  e.preventDefault();
  $('html, body').animate({scrollTop:0}, '300');
});

  