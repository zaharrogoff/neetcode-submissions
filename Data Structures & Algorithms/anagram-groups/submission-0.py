class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        res = list()
        for s in strs:
            key = ''.join(sorted(s))
            if key not in hash:
                hash[key] = []
            hash[key].append(s)
        return list(hash.values())

        