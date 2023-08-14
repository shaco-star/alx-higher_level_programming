#!/usr/bin/node

let arg = 'Arguments found';
if (process.argv[2] === undefined) arg = 'No argument';
if (process.argv.length === 3) arg = 'Argument found';
console.log(arg);
