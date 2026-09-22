"""No-path letter. Empty is stay. Occupancy is cost. Minutes are clock. No live FIRMS."""

from __future__ import annotations

from .route import Node

OFFER = "analog-EVA paper pack $8k–$18k. Not an invoice."
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
