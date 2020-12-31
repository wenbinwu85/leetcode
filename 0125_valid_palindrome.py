from string import ascii_lowercase, digits

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = [c for c in s.lower() if c in ascii_lowercase + digits]
        s2 = ''.join(s2)
        return s2 == s2[::-1]

s = 'acattaca'
answer = Solution().isPalindrome(s)
print(answer)
