#!/usr/bin/node
const Square1 = require('./5-square');
module.exports = class Square extends Square1 {
  charPrint (c) {
    if (typeof c === 'undefined' || !c) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
