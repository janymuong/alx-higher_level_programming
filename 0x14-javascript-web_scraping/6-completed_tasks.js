#!/usr/bin/node

// computes the number of tasks completed by user id; parse data:
// API URL: https://jsonplaceholder.typicode.com/todos

const req = require('request');
const apiUrl = process.argv[2];

req(apiUrl, (err, res, body) => {
  if (!err) {
    const myObj = {};
    const tasks = JSON.parse(body);
    for (const task of tasks) {
      if (task.completed) {
        myObj[task.userId] = myObj[task.userId] ? myObj[task.userId] + 1 : 1;
      }
    }
    console.log(myObj);
  }
});
