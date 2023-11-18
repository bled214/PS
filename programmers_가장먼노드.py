"""
프로그래머스 가장 먼 노드
https://school.programmers.co.kr/learn/courses/30/lessons/49189
"""
from collections import defaultdict, deque

def solution(n, edge):
    answer = 0
    answer_set = set()
    
    graph_dict = defaultdict(set)
    for e in edge:
        start, end = e
        graph_dict[start].add(end)
        graph_dict[end].add(start)

    dis_list = [-1 for _ in range(n+1)]
    q = deque()
    q.append([0, 1])
    dis_list[1] = 0
    dis = 0
    max_dis = 0
    # BFS
    while q:
        # print(q)
        cur_list = q.popleft()
        dis = cur_list[0]
        # 방문한 곳에서 그다음 방문할 노드 큐에 넣기
        for i in range(1, len(cur_list)):
            cur = cur_list[i]
            dis_list[cur] = dis
            tmp = [dis+1]
            for nxt in graph_dict[cur]:
                if dis_list[nxt] == -1:
                    # 거리넣으면서 방문처리 ~ 여기서 해야 중복 방문 없앨 수 있음
                    dis_list[nxt] = dis+1
                    tmp.append(nxt)
            if len(tmp) > 1:
                q.append(tmp)
            else:
                # 더이상 방문할 곳이 없는 곳 => 가장 먼 후보 노드들
                max_dis = max(dis, max_dis)
                answer_set.add((dis, cur))

    for dis, cur in answer_set:
        if dis == max_dis:
            # print(cur)
            answer += 1
    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
