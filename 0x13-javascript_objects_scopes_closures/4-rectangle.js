#!/usr/bin/node

// Rectangle class definition
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // If w or h is not a positive integer, create an empty object
      return {};
    }

    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    // Exchange width and height
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    // Double width and height
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
