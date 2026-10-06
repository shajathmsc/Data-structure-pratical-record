from collections import deque

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


start = int(input("\nEnter starting vertex: "))

visited = [False] * n
queue = deque()

visited[start] = True
queue.append(start)

print("BFS Traversal:", end=" ")

while queue:
    vertex = queue.popleft()

    print(vertex, end=" ")

    for neighbour in graph[vertex]:
        if not visited[neighbour]:
            visited[neighbour] = True
            queue.append(neighbour)

print()