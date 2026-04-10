class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        D = defaultdict(list)

        for u, v in edges:
            D[u].append(v)
            D[v].append(u)
        seen = set()

        def dfs(curr):
            if curr in seen:
                return
            print(f"curr: {curr}")
            seen.add(curr)
            for nei in D[curr]:
                if nei not in seen:
                    dfs(nei)

        
        res = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                res += 1
        return res
