# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None:
            return None
        dic = {}
        temp = UndirectedGraphNode(node.label)
        dic[node.label] = temp
        connect(node,dic)
        
        return temp
def connect(node,dic):
    temp = dic[node.label]
    for n in node.neighbors:
        print("constructing",n.label)
        if n.label not in dic:
            dic[n.label] = UndirectedGraphNode(n.label)
            temp.neighbors.append(dic[n.label])  
            connect(n,dic)
        else:
            temp.neighbors.append(dic[n.label]) 

            
            
