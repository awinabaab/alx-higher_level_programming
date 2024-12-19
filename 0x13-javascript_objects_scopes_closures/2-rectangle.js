#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;

    if ((!w || !h) || (w <= 0 || h <= 0)) {
      delete this.width;
      delete this.height;
    }
  }
}

module.exports = Rectangle;
