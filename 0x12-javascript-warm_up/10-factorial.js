#!/usr/bin/node
// prints factorial of a given number
let n = parseInt(process.argv[2]);
function factorial (n) {
  if (!n || n == 1) {
    return (1);
  }
  return (n * factorial(n - 1));
}

console.log(factorial(n));
