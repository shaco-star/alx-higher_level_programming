#!/usr/bin/node

const req = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
req(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
