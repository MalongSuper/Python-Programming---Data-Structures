# Minimum Spanning Tree using Prim Algorithm and Graph
# starts with a single node and moves through several adjacent nodes
# in order to explore all connected edges along the way.
import heapq


class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):  # Add an edge to the graph
        self.adj[u].append([v, w])
        self.adj[v].append([u, w])  # Since it's an undirected graph

    def prim(self):  # Construct MST using Prim's algorithm
        mst_cost = 0
        mst_edges = []
        visited = [False] * self.v
        min_heap = [(0, 0)]  # Start from the first vertex

        while min_heap:
            weight, u = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            mst_cost += weight

            for v, w in self.adj[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v))
                    mst_edges.append((u, v, w))

        print("Edges in the constructed MST:")
        for u, v, weight in mst_edges:
            print(f"{u} -- {v} == {weight}")
        print("Minimum Spanning Tree cost:", mst_cost)


def main():
    print("Prim's Algorithm")
    vertices = int(input("Enter number of vertices: "))
    edges = int(input("Enter number of edges: "))
    graph = Graph(vertices)
    for i in range(edges):
        u, v, w = map(int, input(f"Edge {i + 1}. Enter u, v, w: ").split(","))
        graph.add_edge(u, v, w)
    # Perform the Prim's Algorithm
    graph.prim()


main()
