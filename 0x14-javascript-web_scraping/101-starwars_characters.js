#!/usr/bin/node

// Write a script that prints all characters of a Star Wars movie
const req = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films';

req.get(`${url}/${movieId}`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const res = JSON.parse(body);
    const idan = res.characters;
    for (let i = 0; i < idan.length; i++) {
      const ohk = idan[i];
      req.get(`${ohk}`, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          const newres = JSON.parse(body);
          console.log(newres.name);
        }
      });
    }
  }
});
