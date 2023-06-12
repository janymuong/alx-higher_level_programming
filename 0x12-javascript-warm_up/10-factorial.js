#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }

  if (n <= 1) {
    return 1;
  }

  return n * factorial(n - 1);
}

const argInt = parseInt(process.argv[2]);

const result = factorial(argInt);
console.log(result);
