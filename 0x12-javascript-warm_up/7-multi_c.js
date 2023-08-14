#!/usr/bin/node

let x = process.argv[2];
if (isNaN(x)) console.log('Missing number of occurrences');
while (x-- && x >= 0) {
  console.log('C is fun');
}
