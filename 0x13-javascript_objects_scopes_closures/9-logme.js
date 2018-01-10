#!/usr/bin/node
exports.logMe = function (item){
  let count = 0;
  let fcn = function () {
    console.log(count+ ':' + item);
    count+=1;}

  fcn();
};
