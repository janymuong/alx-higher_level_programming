#!/usr/bin/node

// module.exports
function addMeMaybe (number, theFunction) {
  number += 1;
  theFunction(number);
}

module.exports.addMeMaybe = addMeMaybe;
