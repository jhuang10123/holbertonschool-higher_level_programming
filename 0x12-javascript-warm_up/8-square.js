#!/usr/bin/node
// prints a square"
let sizeOfSqr = parseInt(process.argv[2]);
if (!sizeOfSqr) {
  console.log('Missing size');
}
for (let i = 0; i < sizeOfSqr; i++) {
  console.log('X'.repeat(sizeOfSqr));
}
