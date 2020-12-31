class Solution:
    def isValid(self, s: str) -> bool:
        left = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                left.append(c)
                continue
            if not left:
                return False
            pair = left.pop() + c
            if pair == '()' or pair =='[]' or pair == '{}':
                continue
            else:
                return False
            
        return left == []
        
answer = Solution().isValid('()')
print(answer)
