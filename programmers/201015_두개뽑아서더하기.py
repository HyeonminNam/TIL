from itertools import combinations

def solution(numbers):
    combination = combinations(numbers, 2)
    answer = [x+y for x, y in combination]
    answer = sorted(list(set(answer)))
    return answer


if __name__ == "__main__":
    numbers = [5, 0, 2, 7]
    print(solution(numbers))