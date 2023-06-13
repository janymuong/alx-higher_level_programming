#!/usr/bin/node

// log count of args and a new arg value.
let argc = 0;

exports.logMe = function (item) {
  console.log(`${argc}: ${item}`);
  argc++;
};
