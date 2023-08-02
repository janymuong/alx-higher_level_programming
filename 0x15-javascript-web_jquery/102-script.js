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
});
// https://fourtonfish.com/hellosalut/?lang=fr redirects to apiUrl which allows CORS
