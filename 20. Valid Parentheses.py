class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False

        stack = deque()
        brackets = dict()
        open_set = {'(', '{', '['}
        brackets[')'] = '('
        brackets['}'] = '{'
        brackets[']'] = '['

        for char in s:
            if char in open_set:
                stack.append(char)
            elif len(stack) > 0 and brackets[char] == stack[-1]:
                stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False