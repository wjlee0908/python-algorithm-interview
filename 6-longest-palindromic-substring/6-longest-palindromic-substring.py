def longestPalindrome(self, s: str) -> str:
    # 투 포인터를 좌우로 확장하며 팰린드롬을 판별한다
    # 리턴값은 가장 긴 팰린드롬
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    # early return
    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    # 문자열을 중앙을 끝까지 이동하며 가장 긴 팰린드롬을 찾는다
    for i in range(len(s) - 1):
        result = max(result,
                     expand(i, i+1), # 짝수 개 팰린드롬
                     expand(i, i+2), # 홀수 개 팰린드롬
                     key=len)

    return result