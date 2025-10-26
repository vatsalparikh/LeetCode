# just changed variable names
class MoreReadableSolution:
    def partitionLabels(self, s: str) -> List[int]:
        char_dict = defaultdict(int)
        for index in range(len(s)):
            char_dict[s[index]] = index

        partitions = []
        start = 0
        while start < len(s):
            end = index = start
            while index <= end:
                end = max(end, char_dict[s[index]])
                index += 1
            partitions.append(end - start + 1)
            start = end + 1
        
        return partitions

'''
start = 24
end = 23
index = 24

create dict
store final occurrences of each char
    while loop and char in s:
        continue the loop until final occurrence of each char
        partition += 1

'''

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_dict = defaultdict(int)
        for index in range(len(s)):
            char_dict[s[index]] = index

        partitions = []
        outer_index = 0
        while outer_index < len(s):
            curr_max_index = par_index = outer_index
            while par_index <= curr_max_index:
                curr_max_index = max(curr_max_index, char_dict[s[par_index]])
                par_index += 1
            partitions.append(curr_max_index - outer_index + 1)
            outer_index = curr_max_index + 1
        
        return partitions

'''
outer_index = 24
curr_max_index = 23
par_index = 24

create dict
store final occurrences of each char
    while loop and char in s:
        continue the loop until final occurrence of each char
        partition += 1

'''