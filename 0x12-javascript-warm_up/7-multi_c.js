#!/usr/bin/node

import { argv } from 'node:process';

let x = argv[2];
if (isNaN(x)) console.log('Missing number of occurrences');
while (x-- && x >= 0) {
  console.log('C is fun');
}
