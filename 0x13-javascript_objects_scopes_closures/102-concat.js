#!/usr/bin/node
const fs = require('fs');
const filesArray = process.argv.slice(2);
const firstSource = filesArray[0];
const secondSource = filesArray[1];
const destination = filesArray[2];

if (!firstSource && !secondSource && !destination) {
  const firstSourceContent = fs.readFile(firstSource, 'utf-8');
  const secondSourceContent = fs.readFile(secondSource, 'utf-8');
  const content = `${firstSourceContent}
${secondSourceContent}`;
  fs.writeFile(destination, content, { flag: 'w' });
}
