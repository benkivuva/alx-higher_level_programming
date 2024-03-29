#!/usr/bin/node
//  a script that computes the number of tasks completed by user id.
const myArray = process.argv.slice(2);
const request = require('request');

request(myArray[0], function (error, response, body) {
  if (error) console.error('error:', error);
  const newDict = {};
  if (JSON.parse(body)) {
    let count = 0;
    let userIdref = 0;
    JSON.parse(body).forEach(dict => {
      if (dict.userId !== userIdref) { userIdref = dict.userId; count = 0; if (dict.completed) { count++; newDict[userIdref] = count; } } else {
        if (dict.completed) { count++; newDict[userIdref] = count; }
      }
    });
  }
  console.log(newDict);
});
