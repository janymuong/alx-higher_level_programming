// 4-script.js
// Toggle the class of the <header> element between "red" and "green" Onclick on the <div id="toggle_header">
$(document).ready(function () {
  $('#toggle_header').click(function () {
    const headerElement = $('header');
    if (headerElement.hasClass('red')) {
      headerElement.removeClass('red').addClass('green');
    } else {
      headerElement.removeClass('green').addClass('red');
    }
  });
});
