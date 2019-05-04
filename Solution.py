class Solution:

    def get_importance_helper(self, employees, id, calculated=[]):
        found_employee_flag = 0
        for emp in employees:
            if emp.id == id:
                employee = emp
                found_employee_flag = 1
        if found_employee_flag == 0:
            raise TypeError("id not in employees list")
        if len(employee.subordinates) == 0:
            return [employee.importance, calculated]
        else:
            sum = 0
            for sub in employee.subordinates:
                if sub not in calculated:
                    calculated.append(sub)
                    sum += self.get_importance_helper(employees, sub, calculated)[0]
            return [employee.importance + sum, calculated]

    def get_importance(self, employees, id):
        return self.get_importance_helper(employees, id, calculated=[])[0]
















