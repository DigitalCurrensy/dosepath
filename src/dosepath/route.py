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
