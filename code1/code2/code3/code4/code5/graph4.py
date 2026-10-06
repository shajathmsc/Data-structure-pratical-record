from collections import deque

n = int(input("Enter number of vertices: "))

graph = [[] for _ in range(n)]

edges = int(input("Enter number of edges: "))

for i in range(edges):
    u, v = map(int, input("Enter edge: ").split())

    graph[u].append(v)
    graph[v].append(u)


source = int(input("Enter source vertex: "))
destination = int(input("Enter destination vertex: "))

visited = [False] * n

queue = deque()

queue.append(source)
visited[source] = True

found = False

while queue:

    vertex = queue.popleft()

    if vertex == destination:
        found = True
        break

    for neighbour in graph[vertex]:

        if not visited[neighbour]:
            visited[neighbour] = True
            queue.append(neighbour)


if found:
    print("Path exists between", source, "and", destination)
else:
    print("Path does not exist")