# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b) if a * b >= 0 else -(-a // b))
            else:
                stack.append(int(char))
        return stack[0]