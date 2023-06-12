#!/usr/bin/node

// this [keyword]: manipulate object props
const myObject = {
  type: 'object',
  value: 12
};

myObject.incr = function () {
  this.value++;
};

console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
