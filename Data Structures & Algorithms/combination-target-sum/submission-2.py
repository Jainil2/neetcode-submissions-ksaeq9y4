class Solution:
    def track(self, i: int, cur: List[int], curSum: int) -> None:
        if curSum == self.target:
            self.res.append(cur[:])
            return
        if curSum > self.target:
            return
        
        for j in range(i, self.length):
            curSum += self.nums[j]
            cur.append(self.nums[j])
            self.track(j, cur, curSum)
            cur.pop()
            curSum -= self.nums[j]
        return

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.nums = nums
        self.length = len(nums)
        self.target = target
        self.res = []
        self.track(0, [], 0)  
        return self.res