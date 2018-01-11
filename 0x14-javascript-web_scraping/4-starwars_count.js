#!/usr/bin/node
// check 5 & 6

const request = require('request');
const url = process.argv[2];
request
  .get(url, function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      let count = 0;
      let WedgeAntilles = 'https://swapi.co/api/people/18/';
      // get list of all films
      let allFilms = JSON.parse(body);
      //      console.log(allFilms);
      // search through each film's 'characters' for char 18
      //      console.log(allFilms)
      for (let i = 0; i < allFilms.results.length; i++) {
        // search character list of each film
        if (allFilms.results[i].characters.includes(WedgeAntilles)) {
          count++;
        }
      }
      console.log(count);
    }
  });
