class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token[0] == "-" and token[1:].isdigit():
                stack.append(int(token))    
            elif token.isdigit():
                stack.append(int(token))
            elif token == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)            
            elif token == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)            
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))           
        return stack[0]
        """
        :type tokens: List[str]
        :rtype: int
        """
        
