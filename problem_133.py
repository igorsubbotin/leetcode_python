# Clone Graph - https://leetcode.com/problems/clone-graph/

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return node
        dummy = UndirectedGraphNode(-1)
        s = [(dummy, node)]
        i = 0
        v = set()
        while i < len(s):
            source, node = s[i]
            i += 1
            clone = UndirectedGraphNode(node.label)
            source.neighbors.append(clone)
            if node.label in v:
                continue
            v.add(node.label)
            for x in node.neighbors:
                s.append((clone, x))
        return dummy.neighbors[0]