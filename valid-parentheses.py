class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        stack=[]
        stack.append(s[0])
        if stack[0]==')' or stack[0]=='}' or stack[0]==']':
            return False
        for i in range(1,n):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack.append(s[i])
            else:
                if len(stack)!=0 and s[i]==")" and stack[-1]=="(":
                    stack.pop()
                elif len(stack)!=0 and s[i]=="]" and stack[-1]=="[":
                    stack.pop()
                elif len(stack)!=0 and s[i]=="}" and stack[-1]=="{":
                    stack.pop()
                else:
                    stack.append(s[i])
        return len(stack)==0


        
