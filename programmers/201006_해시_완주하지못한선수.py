def solution(participant, completion):
    p_dic = {idx:x for idx, x in enumerate(sorted(participant))}
    c_dic = {idx:x for idx, x in enumerate(sorted(completion))}
    for idx in c_dic.keys():
        if p_dic[idx] != c_dic[idx]:
            return p_dic[idx]
    return p_dic[len(p_dic)-1]


if __name__ == "__main__":
    participant_lst = [['leo', 'kiki', 'eden'], ['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['mislav', 'stanko', 'mislav', 'ana']]
    completion_lst = [['eden', 'kiki'], ['josipa', 'filipa', 'marina', 'nikola'], ['stanko', 'ana', 'mislav']]
    for participant, completion in zip(participant_lst, completion_lst):
        print(solution(participant, completion))