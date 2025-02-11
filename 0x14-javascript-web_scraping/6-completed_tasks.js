#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, { json: true }, (error, response, todos) => {
  if (error) console.log(error);

  const taskCount = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (!taskCount[todo.userId]) {
        taskCount[todo.userId] = 0;
      }
      taskCount[todo.userId]++;
    }
  });
  console.log(taskCount);
});
