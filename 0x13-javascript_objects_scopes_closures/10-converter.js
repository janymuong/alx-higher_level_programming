#!/usr/bin/node

// conert base-10 arg to some non-base 10
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
