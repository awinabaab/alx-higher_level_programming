#!/usr/bin/node
const numberOfOccurrences = Math.floor(Number(process.argv[2]));

if (numberOfOccurrences) {
  for (let i = 0; i < numberOfOccurrences; i++) console.log('C is fun');
} else console.log('Missing number of occurrences');
