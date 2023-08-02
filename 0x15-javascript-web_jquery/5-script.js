// 5-script.js
// add a new <li> element to the list <ul class="my_list"> OnClick on the <div id="add_item">
$(document).ready(function () {
  $('#add_item').click(function () {
    const newEl = $('<li></li>').text('Item');
    $('ul.my_list').append(newEl);
  });
});
