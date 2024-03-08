class Solution:
    """
    Input:
    P   A   H   N
    A P L S I I G
    Y   I   R

    s = "PAYPALISHIRING", numRows = 3
    o = "PAHNAPLSIIGYIR"

    Input:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I

    s = "PAYPALISHIRING", numRows = 4
    o = "PINALSIGYAHRPI"

    Input:
    P       H       D
    A     S I     O A
    Y   I   R   T   Y
    P L     I G
    A       N

    s = "PAYPALISHIRINGTODAY", numRows = 5
    o = "PHDASIOAYIRTYPLIGAN"
    """

    # n = 3
    # 0  +4 
    # 1  +2  +2
    # 2  +4 

    # n = 4
    # 0  +6 
    # 1  +4 +2
    # 2  +2 +4
    # 3  +6

    # n = 5
    # 0  +8
    # 1  +6 +2
    # 2  +4 +4
    # 3  +2 +6
    # 4  +8

    def convert(self, s: str, numRows: int) -> str:

        n = numRows
        if len(s) <= n or n < 2:
            return s
        out = ''
        dn = (n - 1) * 2
        for i in range(numRows):
            out += s[i]
            di = (n - i - 1) * 2
            while i + di < len(s):
                if di:
                    i += di
                    out += s[i]
                    # out.append(s[i])
                di = dn - di
                

        return out
                