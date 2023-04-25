#!/usr/bin/node
// A script that counts the number of tasks completed by user id.

const args = process.argv;
let reqURL = args[2];
let req = require('request');
req(reqURL, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    let todos = JSON.parse(body);
    let obj = {};
    for (let i = 0; i < todos.length; i++) {
      let status = (todos[i]['completed']);
      let key = todos[i]['userId'].toString();
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
