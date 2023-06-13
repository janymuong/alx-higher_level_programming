#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // return empty object if w or h not positive
      return {};
    }
  }
}

module.exports = Rectangle;
