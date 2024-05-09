class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = []

        for i in range(len(score)):
            temp.append((score[i],i))

        temp.sort(reverse=True)
        res = [0]*len(score)

        for i in range(len(temp)):
            if i == 0:
                res[temp[i][1]] = "Gold Medal"
            elif i == 1:
                res[temp[i][1]] = "Silver Medal"
            elif i == 2:
                res[temp[i][1]] = "Bronze Medal"
            else:
                res[temp[i][1]] = str(i+1)
        return res