class Solution:
    def nextLargerElement(self, arr):
        # code here
        n= len(arr)
        stack = []
        ans = [0]*n
        curr_max= arr[-1]
        for i in range(n-1,-1,-1):
            curr_ele = arr[i]
            while (len(stack)!=0 and stack[-1]<= curr_ele):
                stack.pop()
            if len(stack)==0:
                ans[i] = -1
            else:
                ans[i] = stack[-1]
            stack.append(curr_ele)
        return ans
