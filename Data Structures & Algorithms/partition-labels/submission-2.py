class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = {}
        for i in range(len(s)):
            if s[i] in mp:
                mp[s[i]][1] = i
            else:
                mp[s[i]] = [i, -1]
        res = []
        last, start = 0, 0
        while start < len(s) and mp[s[start]][1] == -1:
                res.append(1)
                start += 1
                last = start
        if start < len(s):
            ext = mp[s[start]][1]
        while start < len(s):
            while start <= ext:
                ext = max(ext, mp[s[start]][1])
                start += 1
            res.append(start - last)
            last = start
            while start < len(s) and mp[s[start]][1] == -1:
                res.append(1)
                start += 1
                last = start
            if start < len(s):
                ext = mp[s[start]][1]
        return res
