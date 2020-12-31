class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        for i in range(len(s)):
            s_map[s[i]] = s_map.get(s[i], 0) + 1
            s_map[t[i]] = s_map.get(t[i], 0) - 1
        for i in s_map.values():
            if i:
                return False
        return True
            


if __name__ == '__main__':
    s = "a"
    t = "b"

    
    answer = Solution().isAnagram(s, t)
    print(answer)
        