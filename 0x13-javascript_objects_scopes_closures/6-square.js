#!/usr/bin/node

const ParentSquare = require('./5-square');
// Square class definition that inherits from ParentSquare
class Square extends ParentSquare {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }

    // Print the square using the provided character c
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
