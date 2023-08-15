#!/usr/bin/node

// Create instance method charPrint

const SquareParent = require('./5-square.js');

module.exports = class Square extends SquareParent {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
