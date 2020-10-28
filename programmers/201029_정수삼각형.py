
def solution(triangle):
    triangle = [[]] + triangle
    answer = triangle[1][0]
    up_lst = [0] + [triangle[1][0]] + [0]
    for i in range(2, len(triangle)):
        tmp = []
        for idx in range(i):
            tmp.append(max(triangle[i][idx] + up_lst[idx], triangle[i][idx] + up_lst[idx+1]))
        up_lst = [0] + tmp + [0]
        answer = max(tmp)
    return answer


if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(solution(triangle))