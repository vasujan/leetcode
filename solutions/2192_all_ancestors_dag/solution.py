from collections import defaultdict, deque
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        ancestors = defaultdict(set)
        
        for edge in edges:
            node_from, node_to = edge
            graph[node_from].append(node_to)

        for node in range(n):
            queue = deque([node])
            visited = set()
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor in visited:
                        continue
                    ancestors[neighbor].add(node)
                    ancestors[neighbor].update(ancestors[node])
                    queue.append(neighbor)
                    visited.add(neighbor)
        
        ancestors_list = []
        for i in range(n):
            ancestors_list.append(sorted(list(ancestors[i])))
        
        return ancestors_list

