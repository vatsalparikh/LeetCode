class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_string = []
        for char in s.lower():
            if char.isalnum():
                alnum_string.append(char)

        length = len(alnum_string)
        for index in range(length):
            if length % 2 and index > length // 2:
                return True
            elif index >= length // 2:
                return True
            if alnum_string[index] != alnum_string[length - index - 1]:
                return False

        return True
'''
accca

acca
'''