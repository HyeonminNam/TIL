def solution(n, lost, reserve):
    answer = n
    # 체육복 개수 리스트(인덱스 편하게 하기 위해서 앞뒤 패딩)
    clothes = [-1] + [1] * n + [-1]
    # 잃어버렸으나 여분 있는 인원들은 제외하기 위해서 제거
    intersect = set(lost).intersection(set(reserve))
    lost = list(set(lost) - intersect)
    reserve = list(set(reserve) - intersect)
    # 여분 있는 인원들 + 1
    for x in reserve:
        clothes[x] += 1
    for x in lost:
        clothes[x] -= 1
        if clothes[x-1] == 2:
            clothes[x] += 1
            clothes[x-1] -= 1
        elif clothes[x+1] == 2:
            clothes[x] += 1
            clothes[x+1] -= 1
    answer -= clothes.count(0)
    return answer


if __name__ == "__main__":
    n, lost, reserve = 5, [2,3], [3, 4]
    print(solution(n, lost, reserve))