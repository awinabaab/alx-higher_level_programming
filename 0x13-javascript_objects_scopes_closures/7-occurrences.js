#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const incr = 1;
  return list.reduce((acc, curr) => curr === searchElement ? acc + incr : acc, 0);
};
