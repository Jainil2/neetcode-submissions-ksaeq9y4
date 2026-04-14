class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq_s1 = Counter(s1)
        window_size = len(s1)
        freq_window = Counter()

        for i in range(len(s2)):
            freq_window[s2[i]] += 1
            if i >= window_size:
                if freq_window[s2[i - window_size]] == 1:
                    del freq_window[s2[i - window_size]]
                else:
                    freq_window[s2[i - window_size]] -= 1
            if freq_window == freq_s1:
                return True

        return False
