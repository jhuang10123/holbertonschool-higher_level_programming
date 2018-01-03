#!/usr/bin/node
// prints x times "C is fun"
let numOfTimes = parseInt(process.argv[2]);
if (!numOfTimes) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i <= numOfTimes; i++) {
  console.log('C is fun');
}
