// 8-script.js
// Fetch and list the titles of all movies from the URL in the HTML tag <ul id="list_movies">
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (title) {
    const movies = title.results;
    const listMovies = $('#list_movies');

    movies.forEach(function (movie) {
      const listEl = $('<li></li>').text(movie.title);
      listMovies.append(listEl);
    });
  });
});
