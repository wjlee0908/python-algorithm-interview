import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # stones에 나오는 문자 빈도수 계산
        freqs = collections.Counter(stones)
        count = 0

        for char in jewels:
            # counter에서 존재하지 않는 값을 키로 쓰면 0을 반환하므로 에러 처리 안 해도 됨
            count += freqs[char]

        return count