#!/usr/bin/node

//imports an array and computes a new array.


const importedList = require('./100-data.js').list;

const newList = [];

importedList.map((ele, index) => {
  newList.push(ele * index);
});

console.log(importedList);
console.log(newList);
