class Solution:
    def count_NGE(self, a, b):
        # Code here
        n = len(a)
        ans = []
        for i in b:
            count = 0
            for j in range(i+1,n):
                if a[j]>a[i]:
                    count+=1
            ans.append(count) 
        return ans
