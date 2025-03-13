# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stacknums = []
        stackwords = []
        i = 0

        while i < len(s):
            if s[i].isdigit():
                tm = ''
                while s[i].isdigit():  # Read the full number
                    tm += s[i]
                    i += 1
                stacknums.append(int(tm))  # Convert to integer and push to stack

            elif s[i] == '[':
                stackwords.append(s[i])  # Push the opening bracket to stack
                i += 1  # Move to the next character

            elif s[i] == ']':
                temp = ''
                while stackwords and stackwords[-1] != '[':
                    temp = stackwords.pop() + temp  # Build the string to decode
                stackwords.pop()  # Remove the '[' from the stack
                stackwords.append(temp * stacknums.pop())  # Multiply and push back
                i += 1  

            else:
                stackwords.append(s[i])  
                i += 1  

        return ''.join(stackwords)  
