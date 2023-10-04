$(document).ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $('INPUT#btn_translate').click(function () {
    $.ajax({
      url,
      data: { lang: $('INPUT#language_code').val() },
      dataType: 'json',
      crossDomain: true,
      success: function (data) {
        $('DIV#hello').html(data.hello);
      }
    });
  });
});
