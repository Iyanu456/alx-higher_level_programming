#!/usr/bin/node
// A script that display the status code of a GET request

const args = process.argv;
const req = require('request');
req(args[2], function (error, response, body) {
  if (error) {
    console.log('error:', error); // Print the error if one occurred
  } else console.log('code:', response && response.statusCode);
});
