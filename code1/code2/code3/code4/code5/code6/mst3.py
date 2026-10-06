# Minimum Cost using Kruskal's Algorithm

def find(parent, x):

    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]


def union(parent, rank, x, y):

    xroot = find(parent, x)
    yroot = find(parent, y)

    if xroot == yroot:
        return False

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot

    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot

    else:
        parent[yroot] = xroot
        rank[xroot] += 1

    return True


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

for i in range(e):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()

parent = list(range(n))
rank = [0] * n

cost = 0
count = 0

for w, u, v in edges:

    if union(parent, rank, u, v):

        cost += w
        count += 1

        if count == n - 1:
            break

print("Minimum Spanning Tree Cost:", cost)