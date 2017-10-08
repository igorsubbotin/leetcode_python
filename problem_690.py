# 690. Employee Importance - https://leetcode.com/problems/employee-importance
"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        employee = employees[id - 1]
        result = employee.importance
        for sub_id in employee.subordinates:
            result += self.getImportance(employees, sub_id)
        return result