#User function Template for python3
class Solution:
	def reverseSpiral(self, R, C, a):
		# code here
		out = []
		if R == 0:
		    return out
		    
		r_b = 0
		c_b = 0
		r_e = R-1
		c_e = C-1
		
		while (r_b <= r_e) and (c_b <= c_e):
		    for i in range(c_b, c_e+1):
		        out.append(a[r_b][i])
		    
		    r_b+=1
		    for i in range(r_b, r_e+1):
		        out.append(a[i][c_e])
		    c_e-=1
		    if (r_b <=r_e):
		        for i in range(c_e, c_b-1, -1):
		            out.append(a[r_e][i])
		        
		        r_e -=1
		        
		    if (c_b <= c_e):
		        for i in range(r_e, r_b-1, -1):
		            out.append(a[i][c_b])
		        c_b+=1
		        
        return out[::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C=[int(x) for x in input().split()]
        a=[[0]*C for c in range(R)]
        arr=input().split()
        for i in range(R*C):
            a[i//C][i%C]=int(arr[i])
            
        ob=Solution()
        ans=ob.reverseSpiral(R,C,a)
        for i in range(len(ans)):
            print(ans[i],end=" ")
            
        print()
# } Driver Code Ends