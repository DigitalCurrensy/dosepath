# DOSEPATH

For a crew planner who needs a walk across a grid, or a stay.

**Owner:** Digital Currensy Inc.
**Copyright:** 2026 Digital Currensy Inc.
**License:** Apache-2.0. The file named LICENSE is the standard license and is not edited. The copyright notice is in NOTICE and at the top of each source file.

## What it decides

A path, or a stay. No path is a result. If the cheapest walk exceeds the dose cap, that is a stay too.

## The rule

This is a grid search in four directions. Occupancy is the edge cost. Minutes are the steps. The route is the cheapest walk that finishes inside the time. If every walk breaks the clock, or the cheapest walk breaks the dose cap, the desk says stay.

It is not a radiation transport model.

Standing on the start cell is a path of one node when the clock still has time and the dose cap allows a cost of zero. It is not a free wait while the field changes.

## Worked rows

`examples/edges.csv` is a small grid that has a path. It is not a crew timeline a customer sent.

## What it will not do

- Invent a path after the clock runs out.
- Accept a walk whose cost exceeds the dose cap.
- Sign a flight rule.

## Run

```
git clone <this repo>
cd dosepath
PYTHONPATH=src python -m unittest tests.test_kernel
PYTHONPATH=src python -m dosepath examples/edges.csv --start 0,0 --goal 1,0 --t0 0 --tmax 5 --dose-cap 10
```

Python 3.11 or newer. No third-party packages. A path and a stay both exit 0.
