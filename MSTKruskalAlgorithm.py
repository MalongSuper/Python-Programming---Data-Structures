# Minimum Spanning Tree using Kruskal Algorithm and Graph
# Sort all edges of the given graph in increasing order
# Keep adding edge as long as it does not form a cycle

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []

    def add_edge(self, u, v, w):  # Add an edge to graph
        # u: start vertex
        # v: end vertex
        # w: weight
        self.graph.append([u, v, w])  # Since it's a sparse graph

    def find(self, parent, i):  # Find set of an element i
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    @staticmethod
    def union(parent, rank, x, y):  # Union of two sets of x and y
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def kruskal(self):  # Construct MST using Kruskal's algorithm
        result = []  # Store the result of MST
        i = 0  # Index variable used for sorted edges
        e = 0  # Index variable used for result
        # Sort all the edges in ascending order based on their weight
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent, rank = [], []
        # Create v subsets with single elements
        for node in range(self.v):
            parent.append(node)
            rank.append(0)
        # Number of edges to be taken is less than (v - 1)
        while e < self.v - 1:
            u, v, w = self.graph[i]  # Pick the smallest edge and increment
            i = i + 1  # Update the index
            x = self.find(parent, u)
            y = self.find(parent, v)
            # If no cycle encountered, include it in result
            # And increment the index of result for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        # Calculate the minimum cost
        minimum_cost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimum_cost += weight
            print(f"{u} -- {v} == {weight}")
        print("Minimum Spanning Tree:", minimum_cost)


def main():
    print("Kruskal's Algorithm")
    vertices = int(input("Enter number of vertices: "))
    edges = int(input("Enter number of edges: "))
    graph = Graph(vertices)
    for i in range(edges):
        u, v, w = map(int, input(f"Edge {i + 1}. Enter u, v, w: ").split(","))
        graph.add_edge(u, v, w)
    # Perform the Kruskal's Algorithm
    graph.kruskal()


main()
