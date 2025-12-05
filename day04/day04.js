#!/usr/bin/env node

const fs = require("fs");

// Check neighbors around (i,j)
function check(grid, rows, cols, i, j) {
  let nbrcount = 0;
  for (let rowidx = i - 1; rowidx <= i + 1; rowidx++) {
    for (let colidx = j - 1; colidx <= j + 1; colidx++) {
      if (
        !(colidx < 0 ||
          colidx >= cols ||
          rowidx < 0 ||
          rowidx >= rows ||
          (rowidx === i && colidx === j))
      ) {
        if (grid[rowidx][colidx] === "@") {
          nbrcount++;
        }
      }
    }
  }
  return nbrcount;
}

// Part 1: count '@' cells with fewer than 4 neighbors
function part_1(lines) {
  const rows = lines.length;
  const cols = lines[0].length;
  let okays = 0;

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (lines[i][j] === "@" && check(lines, rows, cols, i, j) < 4) {
        okays++;
      }
    }
  }
  return okays;
}

// Part 2: iteratively remove '@' cells with fewer than 4 neighbors
function part_2(lines) {
  const rows = lines.length;
  const cols = lines[0].length;
  let removed = 0;

  while (true) {
    let okays = 0;
    const removelist = [];

    for (let i = 0; i < rows; i++) {
      for (let j = 0; j < cols; j++) {
        if (lines[i][j] === "@" && check(lines, rows, cols, i, j) < 4) {
          okays++;
          removelist.push([i, j]);
        }
      }
    }

    for (const [ri, ci] of removelist) {
      lines[ri][ci] = ".";
    }

    removed += okays;

    if (okays === 0) {
      break;
    }
  }

  return removed;
}

// Convert input lines into grid of characters
function processLines(lines) {
  return lines.map(line => line.split(""));
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
    const lines = raw
      .split("\n")
      .map(line => line.trim())
      .filter(line => line.length > 0);

    console.log(`Read ${lines.length} lines from ${filename}`);
    const grid = processLines(lines);

    console.log("small part 1: 13");
    console.log("Answer part 1: should be 1376", part_1(grid));

    console.log("small part 2: 43");
    console.log("Answer part 2: should be 8587", part_2(grid));
  } catch (err) {
    console.error(`Error reading file: ${err.message}`);
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}
