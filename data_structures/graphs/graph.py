from data_structures.linkedlists.linkedlist import LinkedList


class Graph:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.array = []
        self.__populate_vertices()

    def __populate_vertices(self):
        for _ in range(self.vertices):
            self.array.append(LinkedList())

    def add_edge(self, source, destination):
        if source < 0 or source >= self.vertices or destination < 0 or destination >= self.vertices:
            return

        # directed graph
        self.array[source].insert_at_head(destination)

        # undirected graph
        # self.array[destination].insert_at_head(source)