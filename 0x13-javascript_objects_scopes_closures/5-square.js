#!/usr/bin/node

const Rectangle = require('./4-rectangle');

// class square subclasses rectangle;
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
