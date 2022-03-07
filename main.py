from collections import defaultdict


class Graph:
    def __init__(self, vertices_number):
        self.number_of_vertices = vertices_number
        self.edges = [[-1 for i in range(vertices_number)] for j in range(vertices_number)]  # inititalize matrix
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight


# Function to build the graph
def build_graph():
    edges = [
        ["A", "B"], ["A", "E"],
        ["A", "C"], ["B", "D"],
        ["B", "E"], ["C", "F"],
        ["C", "G"], ["D", "E"]
    ]
    graph = defaultdict(list)

    # Loop to iterate over every
    # edge of the graph
    for edge in edges:
        a, b = edge[0], edge[1]

        # Creating the graph
        # as adjacency list
        graph[a].append(b)
        graph[b].append(a)
    return graph


# after building a graph create different functions to find shortest path

def bruteforce_algorithm(graph_to_traverse, starting_node, end_node):
    already_been = []
    my_queue = [[starting_node]]  # initial node is the start node

    # if the starting node is the same as end node we should return because there is nothing to search for
    if starting_node == end_node:
        return

    while my_queue:
        path = my_queue.pop(0)  # at the start of each iteration pop the last element to then easily get the path
        node = path[-1]

        # Condition to check if the
        # current node is not visited
        if node not in already_been:
            neighbours = graph_to_traverse[node]

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                my_queue.append(new_path)

                # Condition to check if the
                # neighbour node is the goal
                if neighbour == end_node:
                    print("Shortest path = ", *new_path)
                    return
            already_been.append(node)

        # Condition when the nodes
        # are not connected
    print("path does not exist")
    return


def build_djikstra_graph():
    edges = []


if __name__ == "_main_":
    e = Graph
