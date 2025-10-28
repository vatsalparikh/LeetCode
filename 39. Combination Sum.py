class BranchPruningSolution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # pruning branches
        self.combinations = []
        self.backtrack(candidates, target, 0, [])
        return self.combinations

    def backtrack(self, candidates, target, start, combination):
        if target == 0:
            self.combinations.append(combination.copy())
            return
        elif target < 0:
            return

        for index in range(start, len(candidates)):
            if candidates[index] > target: # pruning branches
                break
            combination.append(candidates[index])
            self.backtrack(candidates, target - candidates[index], index, combination)
            combination.pop()

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.combinations = []
        self.backtrack(candidates, target, 0, [])
        return self.combinations

    def backtrack(self, candidates, target, start, combination):
        if target == 0:
            self.combinations.append(combination.copy())
            return
        elif target < 0:
            return

        for index in range(start, len(candidates)):
            combination.append(candidates[index])
            self.backtrack(candidates, target - candidates[index], index, combination)
            combination.pop()