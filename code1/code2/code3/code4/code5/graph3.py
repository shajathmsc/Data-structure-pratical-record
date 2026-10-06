n = int(input("Enter number of vertices: "))

graph = [[] for _ in range(n)]

edges = int(input("Enter number of edges: "))

for i in range(edges):
    u, v = map(int, input("Enter edge: ").split())

    graph[u].append(v)
    graph[v].append(u)


print("\nAdjacency List:")

for i in range(n):
    print(i, "->", graph[i])


visited = [False] * n


def dfs(vertex):

    visited[vertex] = True

    print(vertex, end=" ")

    for neighbour in graph[vertex]:

        if not visited[neighbour]:
            dfs(neighbour)


start = int(input("\nEnter starting vertex: "))

print("DFS Traversal:", end=" ")

dfs(start)

print()