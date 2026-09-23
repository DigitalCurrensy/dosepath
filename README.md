# DOSEPATH

DOSEPATH routes a person through a field that is getting worse, or says that no path exists in the time left.

**Owner:** Digital Currensy Inc.
**License:** Apache-2.0. Our code only. Cited maps stay with their authors.

## What it decides

A path with a running cost, or a stay. No path is a result.

## The rule

Occupancy is the cost. Minutes are the clock. The route is the cheapest walk that finishes inside the time. If every walk breaks the clock or the dose, the desk says stay.

## Worked cases

Four walks stored in this repository: an onset walk, a stay at the peak, a bag that is too tight to carry a path, and a keep-out at a permanently shadowed region. These are the desk’s cases. They are not a crew timeline a customer sent.

## What it will not do

- Invent a path after the clock runs out.
- Treat standing still as free.
- Sign a flight rule.

## Run

```
PYTHONPATH=src python -m unittest tests.test_kernel
```

Notes under `docs/` are the build record. This page is the description.
