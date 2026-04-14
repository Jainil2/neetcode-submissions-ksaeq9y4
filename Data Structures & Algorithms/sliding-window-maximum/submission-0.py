class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = deque()  

        for right in range(len(nums)):
            while window and window[0] <= right - k:
                window.popleft()
            while window and nums[window[-1]] < nums[right]:
                window.pop()
            
            window.append(right)
            if right >= k - 1:
                res.append(nums[window[0]])
        
        return res