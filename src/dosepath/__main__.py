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

"""Route through a cost grid, or stay."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from .route import Node, route


def _node(text: str) -> Node:
    x_text, y_text = text.split(",")
    return int(x_text), int(y_text)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="dosepath",
        description="Route through a cost grid, or stay if the clock or the dose cap breaks.",
    )
    parser.add_argument("csv_path")
    parser.add_argument("--start", required=True)
    parser.add_argument("--goal", required=True)
    parser.add_argument("--t0", type=int, required=True)
    parser.add_argument("--tmax", type=int, required=True)
    parser.add_argument("--dose-cap", type=float, default=None)
    args = parser.parse_args(argv)
    cost: dict[tuple[Node, Node, int], float] = {}
    with Path(args.csv_path).open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            src = (int(row["x1"]), int(row["y1"]))
            dst = (int(row["x2"]), int(row["y2"]))
            cost[(src, dst, int(row["t"]))] = float(row["cost"])
    walked = route(
        cost,
        _node(args.start),
        _node(args.goal),
        t0=args.t0,
        t_max=args.tmax,
        dose_cap=args.dose_cap,
    )
    if walked is None:
        print("stay")
    else:
        dose = 0.0
        tick = args.t0
        for left, right in zip(walked, walked[1:]):
            dose += cost[(left, right, tick)]
            tick += 1
        nodes = " ".join(f"{x},{y}" for x, y in walked)
        print(f"dose={dose:.10g} {nodes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
