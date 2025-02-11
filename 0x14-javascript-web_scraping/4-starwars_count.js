#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, { json: true }, (error, response, body) => {
  if (error) console.log(error);
  else {
    let count = 0;
    body.results.forEach(movie => {
      movie.characters.forEach(character => {
        if (character.includes('18')) count++;
      });
    });
    console.log(count);
  }
});
