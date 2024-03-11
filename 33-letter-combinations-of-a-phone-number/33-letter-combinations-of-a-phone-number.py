from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            """
            문자열을 조합하면서 완성하면 result 리스트에 넣는다
            """
            # 끝까지 탐색하면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return

            # 입력값 자릿수 단위 반복
            for i in range(index, len(digits)):
                # 숫자에 해당하는 모든 문자열 반복
                for char in dic[digits[i]]:
                    dfs(i + 1, path + char)

        if not digits:
            return []

        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "")

        return result
