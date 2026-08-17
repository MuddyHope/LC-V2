class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        parent = [i for i in range(n)]

        def find(node):
            print(f"node: {node}")
            if parent[node] != node:
                parent[node] = find(parent[node])
            print(f"parent: {parent}")
            return parent[node]
       
        def union(u1, u2):
            print(f"u1 : {u1}, u2: {u2}")
            p1 = find(u1)
            p2 = find(u2)
            if p1 == p2:
                return False
                
            parent[p2] = p1
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return False
        return True