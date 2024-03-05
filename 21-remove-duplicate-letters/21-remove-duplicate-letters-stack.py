import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 문자의 개수. 마지막 위치(하나 남았을 때)에 있는 문자면 무조건 넣어야 하기 때문에 생성
        counter = collections.Counter(s)
        # 스택에 들어 있는 문자 집합
        seen = set()
        # 답
        stack = []

        for char in s:
            counter[char] -= 1
            # 중복 방지. 이미 결과에 있는 문자 skip.
            if char in seen:
                continue

            # 더 작은 값으로 시작할 수 있다면 pop
            # 단, 남은 개수가 없으면 마지막 값이므로 못 뺌
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop()) # stack에서 제거했기 때문에 스택 문자 관리하는 seen에서도 제거
            stack.append(char)
            seen.add(char)

        return ''.join(stack)