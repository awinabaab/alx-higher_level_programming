#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, { json: true }, (error, response, movie) => {
  if (error) console.log(error);
  else printCharacters(movie.characters, 0);
});

function printCharacters (characters, idx) {
  if (idx >= characters.length) return;

  request.get(characters[idx], { json: true }, (error, response, character) => {
    if (error) console.log(error);
    else console.log(character.name);
    printCharacters(characters, idx + 1);
  });
}
