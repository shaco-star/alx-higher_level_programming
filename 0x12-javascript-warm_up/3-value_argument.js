#!/usr/bin/node


import { argv } from 'node:process';


let arg = argv[2];
if (argv[2] === undefined) arg = "No argument"
console.log(arg)
