m_len = 0
graph = []
# graph에 문자열 넣어주면서 문자열 최대 길이를 구함
for _ in range(5):
    s = input()
    graph.append(s)
    if len(s) > m_len:
        m_len = len(s)
# graph 문자열에 공백14칸을 추가함
for i in range(5):
    graph[i] = graph[i] + '              '
# 2중 for 문을 돌면서 공백이면 무시하고 아니면 프린트
for i in range(m_len):
    for j in range(5):
        if graph[j][i] == ' ':
            continue
        print(graph[j][i], end='')
# 시간복잡도 O(1)