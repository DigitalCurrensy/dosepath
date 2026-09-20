"""Owned time-binned router. Grid is small on purpose."""
import heapq
from typing import Dict, Tuple

Node = Tuple[int, int]


def route(cost: Dict[Tuple[Node, Node, int], float], start: Node, goal: Node, t0: int, t_max: int) -> list[Node] | None:
    heap = [(0.0, t0, start, [start])]
    seen: set[tuple[Node, int]] = set()
    while heap:
        c, t, n, path = heapq.heappop(heap)
        if n == goal:
            return path
        if t >= t_max or (n, t) in seen:
            continue
        seen.add((n, t))
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nxt = (n[0] + dx, n[1] + dy)
            key = (n, nxt, t)
            if key not in cost:
                continue
            heapq.heappush(heap, (c + cost[key], t + 1, nxt, path + [nxt]))
    return None
