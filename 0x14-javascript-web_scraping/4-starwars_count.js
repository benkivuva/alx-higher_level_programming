#!/usr/bin/node
// Script to count the number of movies featuring "Wedge Antilles"
// Usage: node countMoviesWithWedgeAntilles.js https://swapi-api.alx-tools.com/api/films/

const apiUrl = process.argv[2]; // First argument is the API URL
const characterId = 18; // Character ID for "Wedge Antilles"

const request = require('request');

// Making a GET request to the Star Wars API
request(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode, body.detail);
    return;
  }

  // Filtering movies where Wedge Antilles is present
  const moviesWithWedgeAntilles = body.results.filter(movie => {
    return movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`);
  });

  console.log(moviesWithWedgeAntilles.length);
});
