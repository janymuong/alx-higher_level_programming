// 9-script.js
// Fetch and display the translation of "hello" from the new URL in the HTML tag <div id="hello">
$(document).ready(function () {
  const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  $.get(apiUrl, function (data) {
    $('#hello').text(data.hello);
  });
});

// https://fourtonfish.com/hellosalut/?lang=fr redirects to apiUrl which allows CORS
