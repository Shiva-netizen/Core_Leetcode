#User function Template for python3

class Solution:
    def colName (self, n):
        # your code here
        n-=1
        ans = ""
        while n > 25:
            d = n % 26
            ans += chr(d+65)
            n //= 26
            n-=1
        
        ans += chr(n%26+65)
        
        ans = ans[::-1]
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
    

# } Driver Code Ends