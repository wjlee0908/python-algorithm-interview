from typing import List


def reorderLogFiles(self, logs: List[str]) -> List[str]:
    letters, digits = [], []

    # 문자 로그, 숫자 로그 분류
    for log in logs:
        # 식별자 제외한 첫 번째 단어로 구분
        # `.isdigit()`로 문자열의 숫자 여부 구분
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # 키를 튜플로 매핑해서 첫 번째 정렬 조건, 두 번째 정렬 조건을 지정할 수 있다
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits