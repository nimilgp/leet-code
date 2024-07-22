class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1]
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy.append(candy[i-1] + 1)
            else:
                candy.append(1)
        for i in range(len(ratings) -2, -1,-1):
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i+1]+1,candy[i])
        count = 0
        for c in candy:
            count += c
        return count
