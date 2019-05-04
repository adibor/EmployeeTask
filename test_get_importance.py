from Solution import Solution
import Employee


def test_get_importance():
    e1 = Employee.Employee(1, 1, [2, 3])
    e2 = Employee.Employee(2, 2, [4])
    e3 = Employee.Employee(3, 3, [])
    e4 = Employee.Employee(4, 4, [])

    test_runner = Solution()
    assert test_runner.get_importance([e1, e2, e3, e4], 1) == 10




