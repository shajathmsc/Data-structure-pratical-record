# Prim's Algorithm

INF = 999

n = int(input("Enter number of vertices: "))

print("Enter the adjacency matrix:")

graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

visited = [False] * n
visited[0] = True

total = 0

print("\nMinimum Spanning Tree:")

for k in range(n - 1):

    minimum = INF

    for i in range(n):
        if visited[i]:

            for j in range(n):
                if not visited[j] and graph[i][j] != 0:

                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(x, "--", y, "=", minimum)

    total += minimum
    visited[y] = True

print("\nMinimum Cost:", total)