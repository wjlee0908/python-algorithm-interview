class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 사전 순으로 문자 탐색
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            # 전체 집합이 접미사 집합과 일치하면 답안 후보
            # 답안 조건 맞으면서 사전 순 빠른 문자를 앞에 배치하기 위한 목적
            # 다음으로 사전 순 빠른 문자 찾기 위해서 재귀
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''