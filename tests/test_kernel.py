from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "src"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dosepath.route import route  # noqa: E402
from dosepath.stay import stay_letter  # noqa: E402


class RouteTests(unittest.TestCase):
    def test_path_or_stay(self) -> None:
        start, goal = (0, 0), (1, 0)
        cost = {((0, 0), (1, 0), 0): 1.0}
        path = route(cost, start, goal, t0=0, t_max=4)
        self.assertEqual(path, [(0, 0), (1, 0)])
        stay = stay_letter(route({}, start, goal, t0=0, t_max=2))
        self.assertTrue(stay["empty"])
        self.assertFalse(stay["firms"])
        self.assertLessEqual(stay["words"], 80)
        recovered = stay_letter(path)
        self.assertFalse(recovered["empty"])


if __name__ == "__main__":
    unittest.main()
