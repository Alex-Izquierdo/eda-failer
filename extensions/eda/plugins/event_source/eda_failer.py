"""A source plugin based on range 
https://github.com/ansible/event-driven-ansible/blob/main/extensions/eda/plugins/event_source/range.py
that allows you to generate an exception in a controller way
"""

#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import asyncio
from typing import Any


class EdaFailerExpectedException(Exception):
    """An expected exception for the eda failer plugin"""

    pass


async def main(queue: asyncio.Queue, args: dict[str, Any]) -> None:
    """Generate events with an increasing index i."""
    iterations = args.get("iterations", 5)
    delay = args.get("delay", 1)
    fail_at_index = args.get("fail_at_index", 3)

    for i in range(iterations):
        if i == fail_at_index:
            raise EdaFailerExpectedException("This is a test exception")
        await queue.put({"i": i})
        await asyncio.sleep(delay)
