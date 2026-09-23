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
