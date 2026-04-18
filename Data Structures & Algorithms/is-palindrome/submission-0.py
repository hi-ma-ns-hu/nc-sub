class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ','').lower()
        s = ''.join(i for i in s if i.isalnum())
        return s == s.lower()[::-1]