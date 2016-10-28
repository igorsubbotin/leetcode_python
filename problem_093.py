# Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        if len(s) == 0 or int(s) > 255255255255:
            return res
        res = []
        st = []
        for x, sx in getValid(s):
            st.append(([x], sx))
        while len(st) > 0:
            a, sx = st.pop()
            if len(a) == 4:
                if len(sx) == 0:
                    res.append(".".join([str(x) for x in a]))
                continue
            for y, sy in getValid(sx):
                st.append((a + [y], sy))
        return res
        
def getValid(s):
    n = len(s)
    res = []
    if n == 0:
        return res
    x = int(s[:1])
    res.append((x, s[1:]))
    if n == 1 or x == 0:
        return res
    x = int(s[:2])
    res.append((x, s[2:]))
    if n == 2:
        return res
    x = int(s[:3])
    if x < 256:
        res.append((x, s[3:]))
    return res