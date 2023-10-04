$(document).ready(function () {
  function translate () {
    const lang = $('INPUT#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + lang;
    $.getJSON(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  }

  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) { // Enter key pressed
      translate();
    }
  });
});
