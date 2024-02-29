import collections
from typing import List


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # default value로 [] 리스트를 갖는 dict
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 애너그램은 정렬하면 같은 단어가 된다 -> dict의 key로 사용
        # sorted의 리턴 값은 list. `''.join()`을 이용해서 string으로 변환한다
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())