import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        
        # use queue data structure
        queue = []
        queue.append(root) # initial root
        
        # while queue is not empty
        while len(queue) != 0:
            root = queue.pop(0) # pop first element
            print(root.data, end=" ") # print first element
            
            # recursively add next levels
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)                        
        

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
