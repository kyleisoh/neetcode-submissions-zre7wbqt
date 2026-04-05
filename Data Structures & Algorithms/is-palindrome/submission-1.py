class Solution:
    def isPalindrome(self, s: str) -> bool:

        sanitized_s = ''

        for char in s:
            if char.lower().isalnum():
                sanitized_s += char.lower()               

        print(sanitized_s)
        
        return sanitized_s == sanitized_s[::-1]
        