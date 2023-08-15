#!/usr/bin/node

// Define the function as a property of the exports object
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
