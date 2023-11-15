class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=(2**31-1) or x<=(-2**31):
            return 0
        x=list(str(x))
        if x[0]=='-':
            x=x[1:len(x)]
            x.append('-')
        x.reverse()
        x= int(''.join(x))
        if x>=(2**31-1) or x<=(-2**31):
            return 0
        else:
            return x