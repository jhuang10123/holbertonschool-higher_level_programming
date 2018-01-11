#!/usr/bin/node
// prints all characters of a Star Wars movie
const request = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2] + '/';

request
  .get(url, function (err, response, body) {
    if (err) { console.log(err); } else {
      let film = JSON.parse(body);
      for (let person in film.characters) {
        let characterURL = film.characters[person];
        request.get(characterURL, function (err, response, body) {
          if (err) { console.log(err); } else { console.log(JSON.parse(body).name); }
        });
      }
    }
  }
  );
