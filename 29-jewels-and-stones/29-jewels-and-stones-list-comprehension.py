class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # 리스트의 결과 -> s in jewels의 결과 -> [True, False...]
        return sum([(s in jewels) for s in stones])