class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        processed = []
        x, y, z = 0, 0, 0
        for i in range(len(triplets)):
            if triplets[i][0] <= target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                x = max(x, triplets[i][0])
                y = max(y, triplets[i][1])
                z = max(z, triplets[i][2])
        if [x, y, z] == target:
            return True
        return False