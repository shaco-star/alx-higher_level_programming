$('DIV#add_item').click(function () {
  $('.my_list').append('<li>Item</li>');
});

$('DIV#remove_item').click(function () {
  $('.my_list li:last').remove();
});

$('DIV#clear_list').click(function () {
  $('.my_list').empty();
});
