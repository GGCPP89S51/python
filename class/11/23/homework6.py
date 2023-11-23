class Employee :
    def __init__(self,emp_name=None, emp_id=None, emp_salary=None,emp_department=None) :
        self.emp_id , self.emp_name ,self.emp_salary ,self.emp_deparment = emp_id , emp_name , emp_salary , emp_department

    def assign_department(self,new_department):
        self.emp_deparment = new_department

    def print_employee_details(self) :
        print(self.emp_id,self.emp_name,self.emp_salary,self.emp_deparment)

    def calculate_emp_salary(self,hour = 0):
        hour_salary = self.emp_salary/50
        if hour < 50 :
            return hour_salary * hour
        else:
            overtime = hour - 50
            Overtime_amount = (overtime * hour_salary)
            return hour_salary * hour + Overtime_amount

def main():
    ADAMS = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
    ADAMS.print_employee_details()
    ADAMS.assign_department("RESEARCH")
    ADAMS.print_employee_details()
    print(ADAMS.calculate_emp_salary(60))
    print(ADAMS.calculate_emp_salary(40))

if __name__=='__main__':
    main()