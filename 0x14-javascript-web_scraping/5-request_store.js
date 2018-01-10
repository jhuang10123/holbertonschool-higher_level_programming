#!/usr/bin/node
// ets the contents of a webpage and stores it in a file
const request = require('request');
const fs = require('fs');
request(process.argv[2], 'utf8').pipe(fs.createWriteStream(process.argv[3]));
