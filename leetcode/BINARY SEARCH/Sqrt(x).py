class Solution(object):

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 < x:
                left = mid + 1
            elif mid ** 2 > x:
                right = mid - 1
            else:
                return mid
                # When there is no perfect square, hi is the the value on the left
        return right
