class Solution:
    def isValid(self, s: str) -> bool:
        # while '()' in s or '{}' in s or '[]' in s:
        #     s = s.replace('()', '')
        #     s = s.replace('{}', '')
        #     s = s.replace('[]', '')
        
        # return s == ''

        stack = []
        closing_brackets = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        for b in s:
            if b in closing_brackets:
                if not stack:
                    return False
                open_bracket = stack.pop()
                if closing_brackets[b] != open_bracket:
                    return False
            else:
                stack.append(b)
        
        if stack:
            return False
        return True
