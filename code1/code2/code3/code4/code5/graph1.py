

n = int(input("Enter number of vertices: "))

graph = []

print("Enter the adjacency matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)


# Display Adjacency Matrix
print("\nAdjacency Matrix:")

for row in graph:
    print(row)


# BFS Traversal
def bfs(start):
    visited = [False] * n
    queue = []

    visited[start] = True
    queue.append(start)

    print("BFS Traversal:", end=" ")

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")

        for i in range(n):
            if graph[vertex][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)

    print()



def dfs(vertex, visited):
    visited[vertex] = True
    print(vertex, end=" ")

    for i in range(n):
        if graph[vertex][i] == 1 and not visited[i]:
            dfs(i, visited)



start = int(input("\nEnter starting vertex: "))


bfs(start)


visited = [False] * n

print("DFS Traversal:", end=" ")
dfs(start, visited)
print()