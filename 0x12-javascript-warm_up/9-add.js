#!/usr/bin/node

function add (a, b) {
  const x = Number(process.argv[2]);
  const y = Number(process.argv[3]);

  return (x + y);
}
console.log(add());
