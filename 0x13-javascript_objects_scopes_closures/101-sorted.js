#!/usr/bin/node
// this does not work :(
const data = require('./101-data').dict;
let idList = [];
let newDict = {};

// get list of ids
// add it to key of new dictionary
for (let key in data) {
  if (!idList[data[key]]) {
    idList.push(data[key]);
    newDict[data[key]] = [];
  }
}

// add values to each key
for (let i = 0; i < idList.length; i++) {
  for (let key in data) {
    if (data[key] === idList[i]) {
      newDict[idList].push(key);
    }
  }
}

// let keys = data.keys()
// //.forEach(function(key) {});
// console.log(keys);
// console.log(idList);
