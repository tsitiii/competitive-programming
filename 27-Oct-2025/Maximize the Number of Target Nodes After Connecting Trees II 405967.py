# Problem: Maximize the Number of Target Nodes After Connecting Trees II - https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def build_tree(edges, n):
            tree = defaultdict(list)
            for u, v in edges:
                tree[u].append(v)
                tree[v].append(u)
            return tree
        def compute_parity_counts(tree, n):
            depth = [0] * n
            parent = [-1] * n
            stack = [(0, -1, 0)]
            while stack:
                u, p, d = stack.pop()
                depth[u] = d
                parent[u] = p
                for v in tree[u]:
                    if v != p:
                        stack.append((v, u, d + 1))
            even = [0] * n
            odd = [0] * n
            for i in range(n):
                if depth[i] % 2 == 0:
                    even[0] += 1
                else:
                    odd[0] += 1
            stack = [(0, -1)]
            while stack:
                u, p = stack.pop()
                if p != -1:
                    even[u] = n - even[p]
                    odd[u] = n - odd[p]
                
                for v in tree[u]:
                    if v != p:
                        stack.append((v, u))
            
            return even, odd
        
        n = len(edges1) + 1
        m = len(edges2) + 1
        
        tree1 = build_tree(edges1, n)
        tree2 = build_tree(edges2, m)
        
        even1, odd1 = compute_parity_counts(tree1, n)
        even2, odd2 = compute_parity_counts(tree2, m)
        
        max_odd2 = max(odd2)
        
        return [even1[i] + max_odd2 for i in range(n)]