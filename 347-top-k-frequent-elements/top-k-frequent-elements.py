def based_on_second(elem):
    return elem[1]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = dict()

        for i in nums:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        temp = []
        for i in dict1:
            temp.append((i,dict1[i]))

        temp.sort(key=based_on_second,reverse=True)
        res = []
        for i in range(k):
            res.append(temp[i][0])
        return res