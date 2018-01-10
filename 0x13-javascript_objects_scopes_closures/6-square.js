#!/usr/bin/node
// class Rectangle that defines a rectangle
//module.exports = class Rectangle {
// class Rectangle {
//   constructor (w, h) {
//     if (h > 0 && w > 0) {
//       this.height = h;
//       this.width = w;
//     }
//   }
//   print () {
//     for (let i = 0; i < this.height; i++) {
//       console.log('X'.repeat(this.width));
//     }
//   }
//   rotate () {
//     let temp = this.width;
//     this.width = this.height;
//     this.height = temp;
//   }
//   double () {
//     this.width *= 2;
//     this.height *= 2;
//   }
// };

// class square1 extends Rectangle {
//   constructor(size) {
//     super(size, size);
//   }
// };


const Square1 = require('./5-square');
module.exports = class Square extends Square1 {
  charPrint(c) {
    if (typeof c === 'undefined' || !c) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
