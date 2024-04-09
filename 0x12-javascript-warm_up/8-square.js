#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const size = Number(process.argv[2]);
  for (let i = 0; i < size; i++) {
    let line = '';
    for (let j = 0; j < size; j++ ) {
      line += 'X';
    }
    console.log(line);
  }
}
