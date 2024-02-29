from typing import List
import re
import collections


def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    # 단어를 리스트로 저장
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph) # 구두점 전처리
             .lower().split() # 대소문자 구분 x
             if word not in banned] # 금지된 단어 제외

    # list의 개수를 value로 갖고 있는 dict와 유사한 객체 반환
    # { word1: 3, word2: 2...}
    counts = collections.Counter(words)

    # `[('ball', 2)]`
    return counts.most_common(1)[0][0]