#!/usr/bin/node
const request = require('request');
request
  .get(process.argv[2], function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      let newDict = {};
      // get list of all data
      const allTodos = JSON.parse(body);

      for (let item in allTodos) {
        let each = allTodos[item];
        // check whether user id already in newDict
        if (each.completed === true) {
          if (each.userId in newDict) {
            newDict[each.userId]++;
          } else {
            newDict[each.userId] = 1;
          }
        }
      }
      console.log(newDict);
    }
  });
