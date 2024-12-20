#!/usr/bin/node
let nbOccurrences = 0;
exports.logMe = function (item) {
  console.log(`${nbOccurrences++}: ${item}`);
};
