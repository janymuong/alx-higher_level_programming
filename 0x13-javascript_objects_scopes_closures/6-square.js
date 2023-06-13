#!/usr/bin/node

const SuperSquare = require('./5-square');

// class square subclasses rectangle;
module.exports = class Square extends SuperSquare {
  charPrint (c) {
    // prints the square in terms of char C;
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
};
