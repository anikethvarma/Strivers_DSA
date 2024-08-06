class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26
        for c in word:
            freq[ord(c) - ord('a')] += 1
        
        freq.sort()
        
        totalPushes = 0
        multiplier = 1
        
        for i in range(25, -1, -1):
            if freq[i] == 0:
                break
            
            if (25 - i) % 8 == 0 and i != 25:
                multiplier += 1
            
            totalPushes += freq[i] * multiplier
        
        return totalPushes