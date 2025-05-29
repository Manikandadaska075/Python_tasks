class Solution(object):
    def longestCommonPrefix(self, strs: str )-> str:
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix = strs[0]
        for string in strs[1:]:
            while string.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
strs = list(str(input()).split())
o =Solution()
v = o.longestCommonPrefix(strs)
print(v)