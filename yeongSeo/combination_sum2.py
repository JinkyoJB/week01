# https://leetcode.com/problems/combination-sum-ii/description/
class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []

        self.dfs(sorted(candidates), target, 0, [], res)

        return res
    
    def combi(self, nums, target, idx, path, res):
        if target <= 0:
            if target == 0:
                res.append(path)
            return
        
        """
        정렬했기 때문에 1, 1, 2, 5, 6, 7, 10 과 같은 순서로 들어온다
        """
        for i in range(idx, len(nums)):
            # candi = [1,1,1,1], path = [1,1,1], next element '1' -> 1빼고 1넣어도 [1,1,1]:duplicate
            if i > idx and nums[i] == nums[i-1]:  
                continue
        
            self.dfs(nums, target - nums[i], i + 1, path+[nums[i]], res)

        
        

    
Solution().combinationSum2(
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 27)
