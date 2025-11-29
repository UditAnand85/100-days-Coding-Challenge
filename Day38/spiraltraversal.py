from sys import stdin,setrecursionlimit
from queue import Queue

setrecursionlimit(10**7)
# Binary tree node class for reference 
class BinaryTreeNode :
	def __init__(self, data) :
		self.data = data
		self.left = None
		self.right = None



def spiralOrder(root):

    if not root:
        return []

    s1 = [root]     
    s2 = []         

    ans = []

    while s1 or s2:
        while s1:
            node = s1.pop()
            ans.append(node.data)

            if node.left:
                s2.append(node.left)
            if node.right:
                s2.append(node.right)

        while s2:
            node = s2.pop()
            ans.append(node.data)

            if node.right:
                s1.append(node.right)
            if node.left:
                s1.append(node.left)

    return ans


# Fast input
def takeInput() :
	
    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if(rootData == -1) :
        return None

    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0) :
        currentNode = q.get()  
        
        leftChild = arr[index]
        
        if(leftChild != -1) :
            leftNode =  BinaryTreeNode(leftChild)  
            currentNode.left = leftNode  
            q.put(leftNode)  
        
        index += 1
        rightChild = arr[index]
        
        if(rightChild != -1) :
            rightNode = BinaryTreeNode(rightChild)
            currentNode .right = rightNode  
            q.put(rightNode)  

        index += 1

    return root

# To print the inorder traversal of binary tree
def printSpiral(List1 ) :
    
    for x in List1 :
        print(x,end=" ")

#main

root = takeInput()

List1 = spiralOrder(root)
printSpiral(List1)
