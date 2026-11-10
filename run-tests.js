// Run: node tests/run-tests.js
const c = require("../src/core.js");
const res = c.runTests(new Date());
for (const r of res) console.log(`${r.id} ${r.pass ? "PASS" : "FAIL"}  expected ${r.route.padEnd(9)} got ${r.gotRoute.padEnd(9)} sources: ${r.usedIds.join(", ") || "-"}`);
console.log(`\n${res.filter((r) => r.pass).length}/${res.length} passed`);
