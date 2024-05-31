/* global $ */
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$(document).ready(function () {
  $.get(url, function (data, status) {
    $(data.results).each(function () {
      $('#list_movies').append('<li>' + this.title + '</li>');
    });
  });
});
