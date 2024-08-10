class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l1 = list(pattern)
        l2 = s.split()
        if len(l1) != len(l2):
            return False
        rosetta = {}
        taken = set()
        for i in range(len(l1)):
            char1 = l1[i]
            char2 = l2[i]
            if char1 not in rosetta:
                if char2 in taken:
                    return False
                else:
                    rosetta[char1] = char2
            else:
                if rosetta[char1] != char2:
                    return False    
            taken.add(char2)     
        return True
