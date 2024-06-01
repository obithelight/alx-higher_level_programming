/* global $ */
$(document).ready(function () {
  function fetchTranslation () {
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
  }

  $('#btn_translate').click(function () {
    fetchTranslation();
  });

  $('#language_code').keypress(function (event) {
    if (event.which === 13) { // 13 is the keycode for ENTER
      fetchTranslation();
    }
  });
});
