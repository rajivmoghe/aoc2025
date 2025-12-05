#!/usr/bin/env node

const fs = require("fs");

// Part 1: compute joltage based on left/right max values
function part_1(lines) {
  let joltage = 0;
  for (const aline of lines) {
    let leftidx = 0;
    let leftval = 0;
    let rghtval = 0;

    // find max value and index on the left side
    for (let i = 0; i < aline.length - 1; i++) {
      if (aline[i] > leftval) {
        leftval = aline[i];
        leftidx = i;
      }
    }

    // find max value to the right of that index
    for (let j = leftidx + 1; j < aline.length; j++) {
      if (aline[j] > rghtval) {
        rghtval = aline[j];
      }
    }

    joltage += leftval * 10 + rghtval;
  }
  return joltage;
}

// Helper: get max value at or after _frm, constrained by pos
function get_max_at(line, _frm, pos) {
  let idx = _frm;
  let val = 0;
  for (let i = _frm; i <= line.length - pos; i++) {
    if (line[i] > val) {
      val = line[i];
      idx = i;
    }
  }
  return [idx, val];
}

// Part 2: build 12-digit number from successive maxima
function part_2(lines) {
  let joltage = 0;
  for (const aline of lines) {
    const outvals = [];
    const outidxs = [];
    let stridx = 0;

    for (let j = 12; j > 0; j--) {
      const [idx, val] = get_max_at(aline, stridx, j);
      stridx = idx + 1;
      outvals.push(val);
      outidxs.push(idx);
    }

    const num = parseInt(outvals.map(d => d.toString()).join(""), 10);
    joltage += num;
  }
  return joltage;
}

// Convert input lines into arrays of digits
function processLines(lines) {
  return lines.map(aline => aline.trim().split("").map(d => parseInt(d, 10)));
}

// Main driver
function main() {
  if (process.argv.length !== 3) {
    console.error("Usage: node day02.js <filename>");
    process.exit(1);
  }

  const filename = process.argv[2];

  try {
    const raw = fs.readFileSync(filename, "utf-8");
    const lines = raw.split("\n").filter(line => line.trim().length > 0);

    const parsed = processLines(lines);

    console.log("small part 1: 357");
    console.log("Answer part 1: (should be 17435)", part_1(parsed));
    console.log("small part 2: 3121910778619");
    console.log("Answer part 2: (should be 172886048065379)", part_2(parsed));
  } catch (err) {
    console.error(`Error reading file: ${err.message}`);
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}
