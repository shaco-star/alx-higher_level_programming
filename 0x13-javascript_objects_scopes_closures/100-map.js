#!/usr/bin/node

const importedList = require('./100-data.js').list;

console.log(importedList);
console.log(importedList.map((ele, index) => ele * index));
