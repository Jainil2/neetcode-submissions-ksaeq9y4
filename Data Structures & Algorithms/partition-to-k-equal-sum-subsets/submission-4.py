class Solution:
    def track(self, start, nums, cur, count, k, target, used):
        print()
        if count == k - 1:
            return True
        if cur == target:
            return self.track(0, nums, 0, count + 1, k, target, used)
        for i in range(start, len(nums)):
            if used[i]:
                continue
            if cur + nums[i] > target:
                continue
            used[i] = True
            if self.track(i + 1, nums, cur + nums[i], count, k, target, used):
                return True
            used[i] = False
            if cur == 0:
                break
        return False

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        nums.sort(reverse = True)
        used = [False] * len(nums)
        target = sum(nums) // k
        return self.track(0, nums, 0, 0, k, target, used)