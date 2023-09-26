#!/usr/bin/node
// a script that display the status code of a GET request.
const myArray = process.argv.slice(2);
const request = require('request');

request(myArray[0], function (error, response, body) {
  if (error) console.error('error:', error);
  console.log('code:', response && response.statusCode);
});
