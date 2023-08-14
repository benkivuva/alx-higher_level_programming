#!/usr/bin/node

let y;

if (process.argv.length < 3) {
    y = 'No argument';
} else if (process.argv.length === 3) {
    y = 'Argument found';
} else {
    y = 'Arguments found';
}

console.log(y);
