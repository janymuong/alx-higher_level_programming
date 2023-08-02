// 6-script.js
// update the text of the <header> element to "New Header!!!" Onlick on DIV#update_header
$(document).ready(function () {
  $('#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});
