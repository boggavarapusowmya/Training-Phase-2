class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        for i in range(n-1,-1,-1):
            stack.append(nums[i])
        res = [-1]*n

        for i in range(n-1,-1,-1):
            while stack and stack[-1]>=nums[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(nums[i]) 
        return res               
