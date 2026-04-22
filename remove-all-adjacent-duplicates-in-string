class Solution:
    def removeDuplicates(self, s: str) -> str:
        n=len(s)
        stack=""
        stack+=(s[0])
        for i in range(1,n):
            if len(stack)!=0 and s[i] == stack[-1]:
                stack=stack[:-1]
            else:
                stack+=(s[i])
        return stack
