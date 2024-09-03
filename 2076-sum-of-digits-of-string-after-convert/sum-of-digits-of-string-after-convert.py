class Solution:
    def getLucky(self, s: str, k: int) -> int:
        word = ""
        for i in s:
            word += str(ord(i) - 96)

        
        word = int(word)
        while(k > 0):
            k -= 1
            temp = 0
            while(word):
                temp += word%10
                word = word//10
            word = temp
        return word


