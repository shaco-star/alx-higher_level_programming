#!/usr/bin/node

let arg = 'Argument found';
if (process.argv[2] === undefined) arg = 'No argument';
if (process.argv.length === 3) arg = 'Arguments found';
console.log(arg);
