#!/usr/bin/node
let count = 0;
exports.logMe = function (item) {
//   let fcn = function () {
    console.log(count + ':' + item);
    count++;
//  };
// return fcn();
};
