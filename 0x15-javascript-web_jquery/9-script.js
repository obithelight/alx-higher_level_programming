/* global $ */
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$(document).ready(function () {
  $.get(url, function (data, status) {
    $('#hello').text(data.hello);
  });
});
