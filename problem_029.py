# Divide Two Integers - https://leetcode.com/problems/divide-two-integers/
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend == divisor:
            return 1 * sign
        if divisor > dividend:
            return 0
        if divisor == 1:
            return min(2147483647, dividend * sign)
        i = 1
        t = divisor
        steps = []
        steps.append((divisor, 1))
        current = 0
        direction = 1
        while True:
            t += direction * steps[current][0]
            i += direction * steps[current][1]
            if t <= dividend:
                direction = 1
                if current == len(steps) - 1:
                    steps.append((steps[current][0] + steps[current][0], steps[current][1] + steps[current][1]))
                current += 1
            else:
                direction = -1
                current -= 1
            diff = dividend - t
            if diff >= 0 and diff < divisor:
                return i * sign