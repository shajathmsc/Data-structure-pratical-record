# Minimum Spanning Tree using Prim's Algorithm

INF = 999999

n = int(input("Enter number of vertices: "))

print("Enter the weighted adjacency matrix:")

graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)


visited = [False] * n

visited[0] = True

edges = 0
total_cost = 0

print("\nMinimum Spanning Tree:")

while edges < n - 1:

    minimum = INF
    x = 0
    y = 0

    for i in range(n):

        if visited[i]:

            for j in range(n):

                if not visited[j] and graph[i][j] != 0:

                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(x, "--", y, "=", minimum)

    total_cost += minimum

    visited[y] = True

    edges += 1


print("\nMinimum Cost of Spanning Tree:", total_cost)