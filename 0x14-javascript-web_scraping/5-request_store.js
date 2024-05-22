#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // write to file
    fs.writeFile(file, body, { flag: 'w' }, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
