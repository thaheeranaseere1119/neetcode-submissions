class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = 0
        b = 0
        for digit in num1:
            a = a * 10 + (ord(digit) - ord('0'))
        for digit in num2:
            b = b * 10 + (ord(digit) - ord('0'))
        result = a * b
        return str(result)
        