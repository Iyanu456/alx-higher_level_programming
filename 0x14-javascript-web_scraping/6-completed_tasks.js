#!/usr/bin/node
// A script that counts the number of tasks completed by user id.

const args = process.argv;
const reqURL = args[2];
const req = require('request');
req(reqURL, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const todos = JSON.parse(body);
    const obj = {};
    for (let i = 0; i < todos.length; i++) {
      const status = (todos[i].completed);
      const key = todos[i].userId.toString();
      if (status) {
        if (obj[key]) {
          obj[key]++;
        } else {
          obj[key] = 1;
        }
      }
    }
    console.log(obj);
  }
});
