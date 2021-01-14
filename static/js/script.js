// INITIALIZE MATERIALIZE

/** 
 * Function that initializes materialize side navbar, accordion collapsible,
 * select menu and tabs
 **/
$(document).ready(function() {
    $('.sidenav').sidenav();
    $('.carousel').carousel({
        indicators: true
    });
    $('select').formSelect();
    $('.modal').modal();
});

// BACK TO TOP BUTTON

/**
 * Function implements smooth scrolling back to top after clicking the button
 */

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
    $('html, body').animate({
        scrollTop: 0
    }, '300');
});