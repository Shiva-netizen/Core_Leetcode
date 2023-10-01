#User function Template for python3

class Solution:
    def BoundaryTraversal(self,matrix, n, m):
        if n==1:
            return matrix[0]
        elif n==0:
            return 0
        else:
            to=[]
            nex=[]
            to.extend(matrix[0])
            for i in range(1,n):
                if n==i+1:
                    to.extend(matrix[i][::-1])
                else:
                    if m>1:
                        to.append(matrix[i][-1])
                        nex.append(matrix[i][0])
                    else:
                        to.extend(matrix[i])
            if m>1:
                to.extend(nex[::-1])
            return to





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,m = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(m):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.BoundaryTraversal(matrix,n,m)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends