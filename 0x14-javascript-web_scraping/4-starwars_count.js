#!/usr/bin/node

// prints the number of movies where the character "Wedge Antilles" is present
const req = require('request');

const apiUrl = process.argv[2];

req(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const characterId = 18;
    let count = 0;

    films.forEach((film) => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        count++;
      }
    });

    console.log(count);
  }
});
