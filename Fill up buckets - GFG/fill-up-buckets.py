#User function Template for python3

class Solution:
    def totalWays(self, n, capacity):
        m=1000000007

        p=1

        capacity.sort()

        p=1

        if n==1:
            return capacity[0]

        for i in range(n):
            p=(p*(capacity[i]-i))%m

        return p


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n= int(input())
		capacity = list(map(int,input().split()))
		ob = Solution()
		ans = ob.totalWays(n,capacity)
		print(ans)

# } Driver Code Ends