# Gas Station - https://leetcode.com/problems/gas-station/
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        #print gas, cost
        n = len(gas)
        diff = [0] * n
        for i in xrange(n):
            diff [i] = gas[i] - cost[i]
        if sum(diff) < 0:
            return -1
        i = 0
        j = 0
        fuel = 0
        while j < n:
            fuel += diff[i]
            i = (i + 1) % n
            if fuel < 0:
                j = 0
                fuel = 0
            else:
                j += 1
        return i