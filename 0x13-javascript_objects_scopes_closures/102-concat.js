#!/usr/bin/node
const fs = require('fs');
const filesArray = process.argv.slice(2);
const firstSource = filesArray[0];
const secondSource = filesArray[1];
const destinationFile = filesArray[2];

fs.readFile(firstSource, 'utf-8', (err, firstSourceContent) => {
  if (err) console.error(err);

  fs.readFile(secondSource, 'utf-8', (err, secondSourceContent) => {
    if (err) console.error(err);

    const concatContent = `${firstSourceContent}${secondSourceContent}`;
    fs.writeFile(destinationFile, concatContent, err => { if (err) console.error(err); });
  });
});
