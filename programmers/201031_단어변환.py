from collections import deque

def chain(a, b):
    if sum([1 for i in range(len(a)) if a[i] != b[i]]) == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    # 변환 가능한 단어들 목록 저장
    graph = {}
    for a in words+[begin]:
        graph[a] = []
        for b in words:
            if chain(a, b):
                graph[a].append(b)

    # BFS, target으로 변환하면 단계 return
    visited = {word:False for word in words}
    visited[begin] = True
    queue = deque([[begin, 0]])
    while queue:
        start = queue.popleft()
        for end in graph[start[0]]:
            if end == target:
                return start[1]+1
            elif not visited[end]:
                queue.append([end, start[1]+1])
                visited[end] = True
    # target에 도달하지 못하면 0 return
    return 0

if __name__ == "__main__":
    begin = 'hit'
    target = 'cog'
    words = ['hot', 'dot', 'dog', 'lot', 'log']
    print(solution(begin, target, words))