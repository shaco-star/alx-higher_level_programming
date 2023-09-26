#!/usr/bin/node

const request = require('request');

const url = 'https://jsonplaceholder.typicode.com/todos';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const completedTasks = {};
    data.forEach(element => {
      console.log(element.completed);
      if (element.completed) {
        completedTasks[element.userId]++;
      } else {
        completedTasks[element.userId] = 1;
      }
    });
    console.log(completedTasks);
  }
});
