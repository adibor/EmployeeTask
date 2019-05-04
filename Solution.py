import Employee


class Solution:

    def get_importance(self, employees, id):
        found_employee_flag = 0
        for emp in employees:
            if emp.id == id:
                employee = emp
                found_employee_flag = 1
        if found_employee_flag == 0:
            raise TypeError("id not in employees list")
        if len(employee.subordinates) == 0:
            return employee.importance
        else:
            sum = 0
            for sub in employee.subordinates:
                sum += self.get_importance(employees, sub)
            return employee.importance + sum








