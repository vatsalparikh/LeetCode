class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        s_dict = defaultdict(int)
        for char in s:
            s_dict[char] += 1

        for char in t:
            if char in s_dict:
                s_dict[char] -= 1
            
        for value in s_dict.values():
            if value > 0:
                return False
            
        return True
        