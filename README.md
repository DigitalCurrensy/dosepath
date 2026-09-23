# DOSEPATH

For a crew planner walking people through a radiation field that gets worse while they walk.

**Owner:** Digital Currensy Inc.
**License:** Apache-2.0. Our code only. Cited data and papers stay with their authors.
## What it decides

A path with a running cost, or a stay. No path is a result.

## The rule

Occupancy is the cost. Minutes are the clock. The route is the cheapest walk that finishes inside the time. If every walk breaks the clock or the dose, the desk says stay.

## Worked cases

Four walks stored here: an onset walk, a stay at the peak, a bag too tight to carry a path, and a keep-out in permanent shadow. They are not a crew timeline a customer sent.

## What it will not do

- Invent a path after the clock runs out.
- Treat standing still as free.
- Sign a flight rule.

## Run

```
git clone <this repo>
cd dosepath
PYTHONPATH=src python -m unittest tests.test_kernel
```

Python 3.12. No third-party packages. The test is the demo.
