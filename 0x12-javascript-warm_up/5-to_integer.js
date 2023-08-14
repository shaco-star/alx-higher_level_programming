#!/usr/bin/node

import { argv } from 'node:process';

const number = argv[2];
if (isNaN(number)) { console.log('Not a number'); } else { console.log(`My number: ${number}`); }
