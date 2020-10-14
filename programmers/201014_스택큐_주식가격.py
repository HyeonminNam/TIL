from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    for idx, x in enumerate(prices):
        count = 0
        queue.popleft()
        for y in queue:
            count += 1
            if x > y:
                break
        answer.append(count)
    return answer


if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]
    print(solution(prices))