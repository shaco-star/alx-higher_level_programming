#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, _res, body) => {
  if (err) {
    console.log(err);
  } else {
    const completedTasks = {};
    body = JSON.parse(body);

    body.forEach(task => {
      const { userId, completed } = task;

      if (completed && !completedTasks[userId]) {
        completedTasks[userId] = 0;
      }

      if (completed) ++completedTasks[userId];
    });

    console.log(completedTasks);
  }
});
