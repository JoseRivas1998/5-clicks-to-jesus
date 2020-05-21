class VisitTable:
    def __init__(self):
        self.table = {}

    def visit(self, url):
        self.table[url] = True

    def visited(self, url):
        if url in self.table:
            return True
        return False
