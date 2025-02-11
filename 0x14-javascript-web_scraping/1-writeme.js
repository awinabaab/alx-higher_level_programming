#!/usr/bin/node

const fs = require('fs');

const fileName = process.argv[2];

fs.writeFile(fileName, process.argv[3], 'utf-8', error => {
  if (error) console.log(error);
});
