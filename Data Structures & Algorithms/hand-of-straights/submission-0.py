class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        heapq.heapify(hand)
        if len(hand) % groupSize:
            return False
        
        while hand:
            cur = groupSize - 1
            t = hand[0]
            heapq.heappop(hand)
            temp = []
            while hand and cur > 0:
                if len(hand) < cur:
                    return False
                if hand[0] > t + 1:
                    return False
                elif hand[0] == t:
                    temp.append(heapq.heappop(hand))
                else:
                    t = heapq.heappop(hand)
                    cur -= 1
            if cur > 0:
                return False
            for card in temp:
                heapq.heappush(hand, card)
        return True