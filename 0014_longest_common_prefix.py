class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        common_idx = ''
        for idx, val in enumerate(strs[0]):
            for s in strs[1:]:
                try:
                    if s[idx] != val:
                        return common_idx
                except IndexError:
                    return common_idx
            common_idx += val
        return common_idx
