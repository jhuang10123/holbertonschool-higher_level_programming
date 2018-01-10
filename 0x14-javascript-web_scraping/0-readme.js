#!/usr/bin/node
// reads and prints the content of a file

//syntax for including the File System module in appplication
let fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function(err, data) {
  if (err) {
    console.log(err);
  }
  else {
    console.log(data);
  }
});
