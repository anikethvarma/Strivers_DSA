from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        
        for i in s:
            if i == '{' or i == '[' or i == '(':
                stack.append(i)
            else:
                if len(stack) != 0:
                    temp = stack.pop()
                    if (temp == "(" and i == ")") or (temp == "{" and i == "}") or (temp == "[" and i == "]") :
                        continue
                    else:
                        stack.append(temp)
                        stack.append(i)
                else:
                    stack.append(i)
        if len(stack) != 0:
            return False
        else:
            return True

        