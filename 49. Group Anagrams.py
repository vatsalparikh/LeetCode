
class LessCodeSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            key = ''.join(sorted(string))
            groups[key].append(string)
        return list(groups.values())

class VerboseSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        strs_dict = dict()
        for string in strs:
            sorted_string = str(sorted(string))
            if sorted_string not in strs_dict:
                strs_dict[sorted_string] = [string]
            else:
                value = strs_dict[sorted_string]
                value.append(string)
                strs_dict[sorted_string] = value
        
        for value in strs_dict.values():
            result.append(value)

        return result