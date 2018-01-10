#!/usr/bin/node
exports.esrever = function (list) {
  retList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    retList.push(list[i]);
}
  return retList;
};
