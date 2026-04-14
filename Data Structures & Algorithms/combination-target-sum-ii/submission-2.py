class Solution:
    def track(self, i: int, cur: List[int], curSum: int) -> None:
        if curSum == self.target:
            self.res.append(cur[:])
            return
        if curSum > self.target:
            return
        
        for j in range(i, self.length):
            if j > i and self.nums[j] == self.nums[j - 1]:
                continue

            curSum += self.nums[j]
            cur.append(self.nums[j])
            self.track(j + 1, cur, curSum)
            cur.pop()
            curSum -= self.nums[j]
        return

    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.nums = nums
        self.length = len(nums)
        self.target = target
        self.res = []
        self.track(0, [], 0)  
        return self.res