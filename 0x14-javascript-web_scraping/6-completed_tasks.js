#!/usr/bin/node

// computes the number of tasks completed by user id; parse data:

const req = require('request');

function todoComplete (apiUrl) {
  req(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const tasks = JSON.parse(body);
      const completedTasks = {};

      tasks.forEach((task) => {
        if (task.completed) {
          if (completedTasks[task.userId]) {
            completedTasks[task.userId]++;
          } else {
            completedTasks[task.userId] = 1;
          }
        }
      });

      console.log(completedTasks);
    }
  });
}

const apiUrl = process.argv[2];

todoComplete(apiUrl);
