from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

class Solution:
    def createTree(self, input: List):
        if not input:
            return None
        
        root = Node(input[0])
        queue = [root]
        index = 2
        
        while index < len(input):
            parent = queue.pop(0)
            children = []
            
            while index < len(input) and input[index] is not None:
                child = Node(input[index])
                children.append(child)
                queue.append(child)
                index += 1
            
            parent.children = children
            index += 1
        
        return root
    
    def postorder(self, root: Node) -> List[int]:
        if not root:
            return []
        
        result = []
    
        for child in root.children:
            result.extend(self.postorder(child))
        
        result.append(root.val)
        
        return result

"""
Input: root = [1,null,3,2,4,null,5,6]
"""

"""
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
"""

