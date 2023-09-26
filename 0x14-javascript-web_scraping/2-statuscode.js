#!/usr/bin/node

const req = require('request');

const url = process.argv[2];
req(url, function (err, res) {
  console.log('code:', res.statusCode);
});
