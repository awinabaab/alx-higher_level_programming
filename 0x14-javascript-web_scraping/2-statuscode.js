#!/usr/bin/node

const request = require('request');

const fileName = process.argv[2];

request(fileName, (error, response, body) => {
  if (!error) console.log('code:', response.statusCode);
});
