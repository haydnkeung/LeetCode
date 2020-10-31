class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            print(char)
            if char == '(':
                stack.append(1)
            elif char == '{':
                stack.append(2)
            elif char == '[':
                stack.append(3)
            elif char == ')':
                if len(stack) == 0 or stack[len(stack) - 1] != 1:
                    return False
                else:
                    stack = stack[:-1]
            elif char == '}':
                if len(stack) == 0 or stack[len(stack) - 1] != 2:
                    return False
                else:
                    stack = stack[:-1]
            elif char == ']':
                if len(stack) == 0 or stack[len(stack) - 1] != 3:
                    return False
                else:
                    stack = stack[:-1]
                    
        return len(stack) == 0