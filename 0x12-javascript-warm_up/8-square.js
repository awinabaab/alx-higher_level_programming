#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (size) {
  for (let xAxis = 0; xAxis < size; xAxis++) console.log('X'.repeat(size));
} else console.log('Missing size');
