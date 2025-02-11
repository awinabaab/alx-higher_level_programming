#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, { json: true }, (error, response, body) => {
  if (error) console.log(error);
  else console.log(body.title);
});
