from visit_table import VisitTable


class RelationTable:
    def __init__(self):
        self.table = {}

    def add_relation(self, link_1, link_2):
        if link_1 not in self.table:
            self.table[link_1] = set()
        if link_2 not in self.table:
            self.table[link_2] = set()
        self.table[link_1].add(link_2)
        self.table[link_2].add(link_1)

    def get_unvisited_neighbors(self, url, visit_table: VisitTable):
        neighbors = set()
        if url not in self.table:
            return neighbors
        for neighbor in self.table[url]:
            if not visit_table.visited(neighbor):
                neighbors.add(neighbor)
        return neighbors
