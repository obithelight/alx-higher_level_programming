/* global $ */
$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    $.get(url, function (data, status) {
      if (status === 'success') {
        $('#hello').text(data.hello);
      } else {
        $('#hello').text('An error occurred while fetching data.');
      }
    }).fail(function () {
      $('#hello').text('An error occurred while fetching data.');
    });
  });
});
