#User function Template for python3

from collections import deque

class Solution:
    
    def KDistanceNodes(self, root, target, k):
        
        tr = [None]
        self.addParent(root, None, target, tr)
        
        q = deque()
        q.append((tr[0], 0))
        
        ans = []
        
        while len(q) > 0:
            
            pe = q.popleft()
            
            r, d = pe
            r.visited = True
            
            if d == k:
                ans.append(r.data)
                continue
            
            if r.parent and not r.parent.visited:
                q.append((r.parent, d+1))
            if r.left and not r.left.visited:
                q.append((r.left, d+1))
            if r.right and not r.right.visited:
                q.append((r.right, d+1))
                
        ans.sort()
        
        return ans
        
        
    def addParent(self, root, parent, target, tr):
        
        if not root:
            return
        
        root.parent = parent
        root.visited = False
        
        if tr[0] == None and root.data == target:
            tr[0] = root
        
        self.addParent(root.left, root, target, tr)
        self.addParent(root.right, root, target, tr)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root

if __name__ == "__main__":
    x = Solution()
    t = int(input())
    for _ in range(t):
        line = input()
        target=int(input())
        k=int(input())

        root = buildTree(line)
        res = x.KDistanceNodes(root,target,k)
        
        for i in res:
            print(i, end=' ')
        print()

# } Driver Code Ends