#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (isNaN(size) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  const pstr = 'X'.repeat(size);
  for (let i = 0; i < size; i++) {
    console.log(pstr);
  }
}
