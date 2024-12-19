#!/usr/bin/node
exports.addMeMaybe = function (x, theFunction) {
  const newValue = x + 1;
  theFunction(newValue);
};
