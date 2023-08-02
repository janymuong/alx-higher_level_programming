// jQuery API: update the text color of the <header> el to red (#FF0000)
// when the user clicks on the <div id="red_header">
$(document).ready(function () {
  $('#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
});
