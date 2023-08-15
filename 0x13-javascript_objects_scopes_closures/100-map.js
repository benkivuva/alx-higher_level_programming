#!/usr/bin/node

const list = require('./100-data').list;

// Use the map function to compute a new array
const newList = list.map((value, index) => value * index);

console.log(list);
console.log(newList);
