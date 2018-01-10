#!/usr/bin/node
exports.converter = function (base) {

  return (function(value) {
    return(value.toString(base)); // converts from a number to a hex string
  })
};
