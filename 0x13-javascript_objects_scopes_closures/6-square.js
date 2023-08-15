#!/usr/bin/node

// Create instance method charPrint

const square = require('./5-square');

module.exports = class Square extends square {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }

  charPrint (c = 'X') {
    super.print(c);
  }
};
