#!/usr/bin/node

// (non-built-in reverse )returns the reversed version of a list:
exports.esrever = function (list) {
  return list.map((_, i) => list[list.length - 1 - i]);
};
