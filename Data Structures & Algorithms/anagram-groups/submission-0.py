class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            key = [0]*26
            for i in word:
                idx = (ord(i) - ord('a'))
                key[idx] += 1
            key = tuple(key)
            d[key].append(word)
        return list(d.values())