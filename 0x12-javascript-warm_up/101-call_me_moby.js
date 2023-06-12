#!/usr/bin/node

// function that executes x times a function.
// function must be visible from outside
function callMeMoby (x, theFunction) {
  if (x > 0) {
    theFunction();
    callMeMoby(x - 1, theFunction);
  }
}

module.exports.callMeMoby = callMeMoby;
