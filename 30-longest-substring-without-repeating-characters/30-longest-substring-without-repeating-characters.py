class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0

        for end, char in enumerate(s):
            # sliding window 안에 이미 있는 문자인 지 확인
            # 이미 있으면 start 포인터를 등장 다음 위치로 옮겨서 중복되지 않게 함
            if char in used and start <= used[char]:
                start = used[char] + 1
            else: # longest substring의 길이 갱신
                max_length = max(max_length, end - start + 1)

            # 슬라이딩 윈도우의 새로운 문자 위치를 딕셔너리에 등록
            # 중복 검사용
            used[char] = end

        return max_length