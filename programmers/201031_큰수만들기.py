def solution(number, k):
    answer = ''
    # 각 자릿수 탐색할 범위
    window = [0, k+1]
    for _ in range(len(number)-k):
        max_num = '0'
        # 탐색 범위 내에서 최댓값 뽑아냄
        for idx in range(window[0], window[1]):
            if number[idx] == '9': # 9일 경우 뒤로 넘어가지 않음
                max_num = number[idx]
                window[0] = idx+1
                break
            if number[idx] > max_num:
                max_num = number[idx]
                window[0] = idx+1 # 다음 자릿수에서는 최댓값 뒤에서부터 탐색
        answer += max_num
        window[1] += 1 # 다음 자릿수에서는 끝 범위 +1하여 탐색
    return answer

if __name__ == "__main__":
    number = "1231234"
    k = 3
    print(solution(number, k))