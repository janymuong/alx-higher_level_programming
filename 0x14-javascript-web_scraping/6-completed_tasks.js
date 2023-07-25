#!/usr/bin/node

const req = require('request');

function todosComplete(apiUrl) {
  req(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const tasks = JSON.parse(body);
      const completedTasks = {};

      tasks.forEach((task) => {
        if (task.completed) {
          if (!completedTasks[task.userId]) {
            completedTasks[task.userId] = 1;
          } else {
            completedTasks[task.userId]++;
          }
        }
      });

      let output = '{\n';
      Object.keys(completedTasks).forEach((key) => {
        output += `  '${key}': ${completedTasks[key]},\n`;
      });
      output += '}';

      console.log(output);
    }
  });
}

const apiUrl = process.argv[2];

todosComplete(apiUrl);
