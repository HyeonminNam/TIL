from itertools import permutations

def solution(numbers):
    num_lst = list(numbers)
    prime_lst = []
    # 모든 순열에 대해서 소수 여부 확인
    for i in range(1, len(num_lst)+1):
        p = [int(''.join(papers)) for papers in permutations(num_lst, i) if int(''.join(papers)) > 1]
        for num in p:
            ss = True
            for x in range(2, num//2+1):
                if num%x == 0:
                    ss = False
                    break
            if ss: prime_lst.append(num)
    return len(set(prime_lst))

if __name__ == "__main__":
    numbers = "011"
    print(solution(numbers))