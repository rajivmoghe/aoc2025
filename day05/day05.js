#!/usr/bin/env node

const fs = require("fs");

// Part 1: count how many ingredients fall inside any fresh range
function part_1(freshRanges, things) {
  let freshCount = 0;
  for (const aThing of things) {
    if (freshRanges.some(([start, end]) => aThing >= start && aThing <= end)) {
      freshCount++;
    }
  }
  return freshCount;
}

// Part 2: merge ranges and count total covered integers
function part_2(freshRanges) {
  function mergeRanges(ranges) {
    if (ranges.length === 0) return [];

    // Sort by start (and end for determinism)
    ranges.sort((a, b) => (a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]));

    const merged = [ranges[0]];
    for (let i = 1; i < ranges.length; i++) {
      const [lastStart, lastEnd] = merged[merged.length - 1];
      const [currStart, currEnd] = ranges[i];

      if (currStart <= lastEnd) {
        // overlap/overhang → extend
        merged[merged.length - 1] = [lastStart, Math.max(lastEnd, currEnd)];
      } else {
        // disjoint → new interval
        merged.push([currStart, currEnd]);
      }
    }
    return merged;
  }

  const mergedRanges = mergeRanges(freshRanges);
  let freshCount = 0;
  for (const [start, end] of mergedRanges) {
    freshCount += (end - start) + 1;
  }
  return freshCount;
}

// Parse lines into ranges and ingredients
function processLines(lines) {
  const ranges = [];
  const ingreds = [];
  let readRange = true;

  for (const line of lines) {
    if (!line) {
      readRange = false;
      continue;
    }
    if (readRange) {
      const [start, end] = line.split("-").map(Number);
      ranges.push([start, end]);
    } else {
      ingreds.push(Number(line));
    }
  }
  return [ranges, ingreds];
}

// Main driver
function main() {
  if (process.argv.length !== 3) {
    console.error("Usage: node day02.js <filename>");
    process.exit(1);
  }

  const filename = process.argv[2];
  try {
    const lines = fs.readFileSync(filename, "utf-8")
      .split("\n")
      .map(line => line.trim());

    console.log(`Read ${lines.length} lines from ${filename}`);
    const [fresh, stuff] = processLines(lines);

    console.log("small part 1: should be 3 →", part_1(fresh, stuff));
    console.log("small part 2: should be 14 →", part_2(fresh));
    // Example big answer
    console.log("Answer part 1: should be 885 →", part_1(fresh, stuff));
    console.log("Answer part 2: should be 348115621205535 →", part_2(fresh));

  } catch (err) {
    console.error(`Error reading file: ${err.message}`);
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}
