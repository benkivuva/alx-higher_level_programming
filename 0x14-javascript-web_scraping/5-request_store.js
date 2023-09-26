#!/usr/bin/node
// Script to fetch webpage content and store it in a file
const myArray = process.argv.slice(2);
const request = require('request');
const fs = require('fs');

request(myArray[0], function (error, response, body) {
  if (error) console.error('error:', error);
  fs.writeFile(myArray[1], body, (err, data) => {
    if (err) console.log(err);
  });
});
