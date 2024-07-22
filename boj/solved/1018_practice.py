N = 10
M = 13

for i in range(N - 7):
    for j in range(M - 7):
        graph = [[0] * M for _ in range(10)]
        for dy in range(8):
            for dx in range(8):
                graph[i + dy][j + dx] = 1

        for line in graph:
            print(line)
        print('--------------------------------------------')