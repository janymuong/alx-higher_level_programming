// JQuery API:
$(document).ready(function () {
  function getTargetLanguageTxt () {
    const sourceLanguageCode = $('#language_code').val();
    const apiUrl = `https://hellosalut.stefanbohacek.dev/?lang=${sourceLanguageCode}`;

    // make the API request to fetch the translation
    $.get(apiUrl, function (data) {
      $('#hello').text(data.hello);
    });
  }

  // OnClick event - a "Translate" button
  $('#btn_translate').click(function () {
    getTargetLanguageTxt();
  });

  // OnKeyPress event - press ENTER in #language_code
  $('#language_code').keypress(function (event) {
    if (event.which === 13) { // Check if the pressed key is ENTER (key code 13)
      getTargetLanguageTxt();
    }
  });
});
// https://fourtonfish.com/hellosalut/?lang=fr redirects to apiUrl which allows CORS
