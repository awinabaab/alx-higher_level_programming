#!/usr/bin/node
const array = process.argv.slice(2);
const sortedArray = array.sort((a, b) => b - a);

if (array.length < 2) console.log(0);
else console.log(sortedArray[1]);
