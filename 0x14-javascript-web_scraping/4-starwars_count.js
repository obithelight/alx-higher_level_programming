#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const actor = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (err, res, data) => {
  if (err) {
    console.error(err);
  } else {
    try {
      const films = JSON.parse(data).results;
      const match = films.filter((film) => film.characters.includes(actor));
      console.log(match.length); // Corrected typo here
    } catch (error) {
      console.error('Error parsing JSON data:', error);
    }
  }
});
