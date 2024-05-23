#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, function (error, res, data) {
  if (error) {
    console.log(error);
    return;
  }
  const actors = JSON.parse(data).characters;
  actors.forEach(actor => {
    request(actor, (error, res, body) => {
      if (error) {
        console.log(error);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  });
});
