class Solution:
    def isValid(self, s):
        list1 = []
        d = {')': '(', ']': '[', '}': '{'}
        
        for i in s:
            if i in d:
                if list1 and list1[-1] == d[i]:
                    list1.pop()  
                else:
                    return False  
            else:
                list1.append(i)
        return not list1
s = str(input(""))  
o = Solution()
v = o.isValid(s)
print(v)