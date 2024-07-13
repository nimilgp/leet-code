class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            signature = ''.join(sorted(word))
            if signature not in hashmap:
                hashmap[signature] = [word]
            else:
                hashmap[signature].append(word)
        return list(hashmap.values())
