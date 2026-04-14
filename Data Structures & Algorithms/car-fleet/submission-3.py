class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        for p, s in pairs:
            cur = (target - p) / s
            if stack and stack[-1] >= cur:
                continue
            stack.append(cur)
        return len(stack)