#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const fileName = process.argv[3];

request.get(url, (error, response, body) => {
  if (!error) {
    fs.writeFile(fileName, body, 'utf-8', error => error ? console.log(error) : {});
  }
});
