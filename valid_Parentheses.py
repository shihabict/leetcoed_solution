class Solution:
    def isValid(self, s):
        l = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                l.append(i)
            elif len(l) <= 0:
                return False
            elif i == ')' and l.pop() != '(':
                return False
            elif i == '}' and l.pop() != '{':
                return False
            elif i == ']' and l.pop() != '[':
                return False
        if len(l) == 0:
            return True
        else:
            return False


sol = Solution()
print(sol.isValid("{ { ( { } ) } }"))
