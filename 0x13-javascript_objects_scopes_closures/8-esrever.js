#!/usr/bin/node
exports.esrever = function (list) {
  return list.map((value, index, array) => array[array.length - 1 - index]);
};
