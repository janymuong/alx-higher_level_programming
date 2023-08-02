// JQuery API:
$(document).ready(function () {
  function addListEl () {
    const newEl = $('<li>Item</li>');
    $('ul.my_list').append(newEl);
  }
  function removeEl () {
    $('ul.my_list li:last-child').remove();
  }
  function clearList () {
    $('ul.my_list').empty();
  }

  // OnClick eventt: "Add item" <div>
  $('#add_item').click(function () {
    addListEl();
  });
  // OnClick event: "Remove item" <div>
  $('#remove_item').click(function () {
    removeEl();
  });
  // OnClick event - "Clear list" <div>
  $('#clear_list').click(function () {
    clearList();
  });
});
