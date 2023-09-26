#!/usr/bin/node
// Script that prints the title of a Star Wars movie
const myArray = process.argv.slice(2);
const request = require('request');

if (Number.isInteger(parseInt(myArray[0]))) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${myArray[0]}`;
  request(apiUrl, function (error, response, body) {
    if (error) console.error('error:', error);
    console.log(JSON.parse(body).title);
  });
}
