class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''
        for char in s:
            if char.isalnum():
                temp += char
        strvar = temp.casefold()
        return strvar == strvar[-1::-1]

obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))
print(obj.isPalindrome("race a car"))
print(obj.isPalindrome(" "))
