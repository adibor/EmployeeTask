from Solution import Solution
import Employee
import pytest


def test_get_importance():
    e1 = Employee.Employee(1, 1, [2, 3, 4])
    e2 = Employee.Employee(2, 2, [4])
    e3 = Employee.Employee(3, 3, [4, 5])
    e4 = Employee.Employee(4, 4, [])
    e5 = Employee.Employee(5, 5, [4])
    e6 = Employee.Employee(6, 6, [5, 4, 1, 2, 3, 7])
    e7 = Employee.Employee(7, 0, [])
    e8 = Employee.Employee(8, 0, [5])
    test_runner = Solution()
    assert test_runner.get_importance([e1, e2, e3, e4, e5, e6, e7, e8], 1) == 15   #Test the case when an employee (4) is a subordinate of 2 or mpre employees(1, 2, 3)- the employee's value should be calculated only once
    assert test_runner.get_importance([e1, e2, e3, e4, e5, e6, e7, e8], 2) == 6
    assert test_runner.get_importance([e1, e2, e3, e4, e5, e6, e7, e8], 3) == 12
    assert test_runner.get_importance([e1, e2, e3, e4, e5, e6, e7, e8], 4) == 4
    assert test_runner.get_importance([e1, e2, e3, e4, e5, e6, e7, e8], 5) == 9
    assert test_runner.get_importance([e1, e2, e3, e4, e5, e6, e7, e8], 6) == 21
    assert test_runner.get_importance([e1, e2, e3, e4, e5, e6, e7, e8], 7) == 0
    assert test_runner.get_importance([e1, e2, e3, e4, e5, e6, e7, e8], 8) == 9
    with pytest.raises(Exception):
        assert test_runner.get_importance([e1, e2, e3, e4, e5, e6, e7, e8], 9)    #Test if an id (9) not in employees list raises an error
        assert test_runner.get_importance([e1, e2, e3], 1)    #Test if an id (4- subordinate of employee #1) is not in the employees list raises an error









