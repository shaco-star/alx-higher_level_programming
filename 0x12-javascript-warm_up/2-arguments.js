#!/usr/bin/node

import { argv } from 'node:process';

let arg = 'Argument found';
if (argv[2] === undefined) arg = 'No argument';
console.log(arg);
