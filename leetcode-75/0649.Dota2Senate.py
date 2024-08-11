class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = []
        dire = []
        n = len(senate)
        for i in range(len(senate)):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(n)
            else:
                dire.append(n)
            dire.pop(0)
            radiant.pop(0)
            n += 1
        if radiant:
            return "Radiant"
        else:
            return "Dire"
