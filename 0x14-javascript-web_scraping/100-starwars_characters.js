#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, { json: true }, (error, response, movie) => {
  if (error) console.log(error);
  else {
    movie.characters.forEach((character, idx) => {
      request.get(character, { json: true }, (error, response, character) => {
        if (!error) console.log(character.name);
      });
    });
  }
});
