#!/usr/bin/node

const req = require('request');

const url = process.argv[2];
req(url, function (err, res) {
  if (err) {
    console.log(err);
  }
  console.log('code:', res.statusCode);
});
