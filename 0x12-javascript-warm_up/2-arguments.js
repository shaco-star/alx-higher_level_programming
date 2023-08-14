#!/usr/bin/node

let arg = 'Argument found';
if (process.argv[2] === undefined) arg = 'No argument';
console.log(arg);
