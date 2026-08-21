class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # union-find
        parent = [i for i in range(n)]

        rank = [0] * (n)

        def find(node):
            # print(f"node: {node}")
            # finding the parent
            if node != parent[node]:
                parent[node] = find(parent[node])
            # print(f"node: {node}, parent: {parent[node]}")
            return parent[node]
        

        def union(u1, u2):
            p1 = find(u1)
            p2 = find(u2)

            if p1 == p2:
                return

            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p1] < rank[p2]:
                parent[p1] = p2
            else:
                parent[p2] = p1
                rank[p1] += 1
            # print(f"parent: {parent},\nrank: {rank}")

        for u1, u2 in edges:
            union(u1, u2)
        print(parent)

        roots = set()

        for i in range(n):
            roots.add(find(i))

        return len(roots)



