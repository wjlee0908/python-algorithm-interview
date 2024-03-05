class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # 닫는 괄호에 맞는 여는 괄호 쌍
        table = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        # 스택 이용 예외 처리 및 일치 여부 판별
        for char in s:
            if char not in table: # 여는 괄호는 쌓는다
                stack.append(char)
            elif not stack or table[char] != stack.pop(): # 닫는 괄호이면 일치 여부 확인
                return False
        return len(stack) == 0