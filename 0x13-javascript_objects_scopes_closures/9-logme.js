#!/usr/bin/node

let numPrinted = 0;

// Define the function as a property of the exports object
exports.logMe = function (item) {
  console.log(`${numPrinted}: ${item}`);
  numPrinted++;
};
