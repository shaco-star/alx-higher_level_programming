#!/usr/bin/node

// Convert number from base 10 to another base

exports.converter = function (base) {
  function myConverter (n) {
    return n.toString(base);
  }
  return myConverter;
};
