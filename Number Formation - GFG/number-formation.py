#User function Template for python3
class Solution:
    def getSum(self, x, y, z):
        mod = (10**9)+7 
        
        # exactsum[i][j][k] stores the sum of 
        # all the numbers having exact 
        # i 4's, j 5's and k 6's 
        exactsum = [] 
        
        # exactnum[i][j][k] stores numbers 
        # of numbers having exact 
        # i 4's, j 5's and k 6's 
        exactnum = []
        
        for i in range(x+1):
            two = []
            two1 = []
            for j in range(y+1):
                temp = [0]*(z+1)
                temp1 = [0]*(z+1)
                two.append(temp)
                two1.append(temp1)
            exactnum.append(two)
            exactsum.append(two1)
        
        ans = 0
        exactnum[0][0][0] = 1
        
        
        for i in range(x+1):
            for j in range(y+1):
                for k in range(z+1):
                
                    # Computing exactsum[i][j][k] 
                    # as explained above 
                    if (i > 0):
                        exactsum[i][j][k] += (exactsum[i - 1][j][k] * 10 + 4 * exactnum[i - 1][j][k]) % mod 
                        exactnum[i][j][k] += exactnum[i - 1][j][k] % mod
                    if (j > 0):
                        exactsum[i][j][k] += (exactsum[i][j - 1][k] * 10 + 5 * exactnum[i][j - 1][k]) % mod 
                        exactnum[i][j][k] += exactnum[i][j - 1][k] % mod 
                    if (k > 0):
                        exactsum[i][j][k] += (exactsum[i][j][k - 1] * 10 + 6 * exactnum[i][j][k - 1]) % mod 
                        exactnum[i][j][k] += exactnum[i][j][k - 1] % mod
                    
                    ans += exactsum[i][j][k] % mod
                    ans %= mod 
            
        return int(ans)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		X,Y,Z = map(int,input().split())
		ob = Solution()
		ans = ob.getSum(X,Y,Z)
		print(ans)
# } Driver Code Ends