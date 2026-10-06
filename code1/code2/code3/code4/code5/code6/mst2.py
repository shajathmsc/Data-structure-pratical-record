# Kruskal's Algorithm

def find(parent, i):
    while parent[i] != i:
        i = parent[i]
    return i


def union(parent, x, y):
    parent[x] = y


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter source, destination and weight:")

for i in range(e):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

# Sort edges according to weight
edges.sort()

parent = list(range(n))

mst = []
cost = 0

for w, u, v in edges:

    x = find(parent, u)
    y = find(parent, v)

    if x != y:
        mst.append((u, v, w))
        cost += w
        union(parent, x, y)

print("\nMinimum Spanning Tree:")

for u, v, w in mst:
    print(u, "--", v, "=", w)

print("Minimum Cost:", cost)