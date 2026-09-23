# Copyright 2026 Digital Currensy Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Owned time-binned router. Grid is small on purpose."""
import heapq
import math
from typing import Dict, Tuple

Node = Tuple[int, int]


def route(
    cost: Dict[Tuple[Node, Node, int], float],
    start: Node,
    goal: Node,
    t0: int,
    t_max: int,
    dose_cap: float | None = None,
) -> list[Node] | None:
    if start == goal:
        if t0 <= t_max and (dose_cap is None or 0 <= dose_cap):
            return [start]
        return None
    heap = [(0.0, t0, start, [start])]
    seen: set[tuple[Node, int]] = set()
    while heap:
        c, t, n, path = heapq.heappop(heap)
        if n == goal:
            if dose_cap is not None and c > dose_cap:
                return None
            return path
        if t >= t_max or (n, t) in seen:
            continue
        seen.add((n, t))
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            nxt = (n[0] + dx, n[1] + dy)
            key = (n, nxt, t)
            if key not in cost or not math.isfinite(cost[key]) or cost[key] < 0:
                continue
            heapq.heappush(heap, (c + cost[key], t + 1, nxt, path + [nxt]))
    return None
