from itertools import combinations

def solution(phone_book):
    # 두 개를 뽑아서 접두어 확인
    for x, y in combinations(phone_book, 2):
        # 짧은 번호 길이만큼 잘라서 일치 여부 확인
        shorter = min(len(x), len(y))
        if x[:shorter]==y[:shorter]:
            return False
    return True

if __name__ == "__main__":
    phone_book = ['119', '97674223', '1195524421']
    print(solution(phone_book))