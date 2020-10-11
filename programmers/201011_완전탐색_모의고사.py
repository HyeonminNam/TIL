def solution(answers):
    pat_1 = [1, 2, 3, 4, 5]
    pat_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pat_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    lst = [0, 0, 0]
    for idx in range(len(answers)):
        if answers[idx] == pat_1[idx%len(pat_1)]:
            lst[0] += 1
        if answers[idx] == pat_2[idx%len(pat_2)]:
            lst[1] += 1
        if answers[idx] == pat_3[idx%len(pat_3)]:
            lst[2] += 1
    maximum = max(lst)
    answer = []
    for i in range(3):
        if lst[i] == maximum:
            answer.append(i+1)    
    return answer



if __name__ == "__main__":
    answers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    print(solution(answers))