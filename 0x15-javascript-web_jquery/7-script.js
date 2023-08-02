// 7-script.js
// tetch character name from URL and display it in the HTML tag <div id="character">
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (charname) {
    $('#character').text(charname.name);
  });
});
