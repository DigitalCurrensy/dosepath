# DOSEPATH whitepaper

## The job
A solar particle event, a fire front, or a dust storm moves. A person must reach a shelter, a road, or a lander. The product is the path whose integrated load stays under a limit, or a statement that no such path exists in the time left.

## Method
Graph of walkable cells. Edge cost = distance + time-varying field (dose, heat, smoke). Recompute as the field updates. Output path + arrival time + remaining margin.

Earth first: fire front + roads + a named shelter. Moon later: same solver, SPE field + shelter bag.
