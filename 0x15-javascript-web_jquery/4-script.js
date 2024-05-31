/* global $ */
$(document).ready(function () {
  $('#toggle_header').on('click', function () {
    const element = $('header');
    if (element.hasClass('red')) {
      element.removeClass('red').addClass('green');
    } else {
      element.removeClass('green').addClass('red');
    }
  });
});
