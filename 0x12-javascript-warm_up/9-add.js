#!/use/bin/node

import { argv } from 'node:process';

function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

add(argv[2], argv[3]);
