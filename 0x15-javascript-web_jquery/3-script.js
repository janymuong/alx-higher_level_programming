// add the class "red" to the <header>
// with click click event on the <div id="red_header">
$(document).ready(function () {
  $('#red_header').click(function () {
    $('header').addClass('red');
  });
});
