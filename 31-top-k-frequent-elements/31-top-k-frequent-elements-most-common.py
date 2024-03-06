import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # collections.Counter(nums).most_common(k) => [(1, 3번), (2, 2번)]
        # * => unpack => (1, 3번), (2, 2번)
        # zip => 세로로 묶기 => (1, 2), (3번, 2번)
        return list(zip(*collections.Counter(nums).most_common(k)))[0]