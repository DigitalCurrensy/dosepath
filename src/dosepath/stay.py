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

"""No-path letter. Empty is stay. Occupancy is cost. Minutes are clock. No live FIRMS."""

from __future__ import annotations

from .route import Node

OFFER = "Unsigned. Not an invoice."
GOLDEN = ["TRPO", "HAMM", "KAWE", "LEMO", "WOOD"]


def stay_letter(path: list[Node] | None) -> dict:
    empty = path is None
    body = (
        "DOSEPATH. No path in the time left. Empty is stay. "
        "Witness names the min-load walk and is not the product. No live FIRMS. Not medical."
        if empty
        else (
            "DOSEPATH. Path recovered. Occupancy is cost. Minutes are clock. "
            "No wait action. Not flight software. Not medical. FIRMS unfetched."
        )
    )
    return {
        "empty": empty,
        "path": path,
        "body": body,
        "words": len(body.split()),
        "golden": GOLDEN,
        "firms": False,
        "medical": False,
        "offer": OFFER,
    }
