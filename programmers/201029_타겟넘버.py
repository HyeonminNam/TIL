from itertools import combinations

def solution(numbers, target):
    answer = 0
    total = sum(numbers)
    for n in range(0, len(numbers)+1):
        # 더할 수들의 조합
        plus_lst = combinations(numbers, n)
        for plus in plus_lst:
            # total - 더할 수들의 합 = 뺄 수들의 합
            # 최종 계산 결과  = 더할 수들의 합 - 뺄 수들의 합(= total - 더할 수들의 합)
            result = sum(plus) - (total - sum(plus))
            if result == target:
                answer += 1
    return answer


if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    target = 3
    print(solution(numbers, target))