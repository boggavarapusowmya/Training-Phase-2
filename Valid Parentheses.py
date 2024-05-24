class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openbrac = ['(','{','[']
        for ch in s:
            if ch in openbrac:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                if ch == ')':
                    if stack[-1]!= '(':
                        return False
                    stack.pop()    
                elif ch == ']':
                    if stack[-1]!='[':
                        return False
                    stack.pop()    
                elif ch == '}':
                    if stack[-1]!='{':
                        return False  
                    stack.pop()
        if len(stack)!=0:
            return False
        return True