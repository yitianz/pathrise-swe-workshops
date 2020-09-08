class UF:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def union(i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j