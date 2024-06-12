class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                temp += i.lower()

        left = 0
        right = len(temp) - 1
        while(left <= right):
            if temp[left] != temp[right]:
                return False
            left += 1
            right -= 1
        return True