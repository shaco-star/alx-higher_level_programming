#!/usr/bin/node

import { argv } from 'node:process';

const size = argv[2];
if (isNaN(size)) console.log('Missing size');
for (let i = 0; i < size; i++) {
  let row = '';
  for (let j = 0; j < size; j++) {
    row += 'x';
  }
  console.log(row);
}
