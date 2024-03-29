# the idea is when we have multiple child classes that inherit fromm the same parent then
# there can be a class that contains other classes

from abc import ABCMeta, abstractstaticmethod, abstractmethod

class IDepartment(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, emps):
        pass

    @abstractstaticmethod
    def print_department():
        """implemented in child class"""
        
class Accounting(IDepartment):
    def __init__(self, emps):
        self.emps = emps
        
    def print_department(self):
        print("This is accounting department")
        print(f"Number of employees: {self.emps}")
        
    def __repr__(self):
        return "Accounting Department"
        
class DataScience(IDepartment):
    def __init__(self, emps):
        self.emps = emps
        
    def print_department(self):
        print("This is Data Science department")
        print(f"Number of employees: {self.emps}")
    def __repr__(self):
        return "Data Science Department"
        
class ParentDepartment(IDepartment):
    def __init__(self, emps):
        self.emps = emps
        self.base_emps = emps
        self.sub_depts = []
        
    def add_dept(self, dept):
        self.sub_depts.append(dept)
        self.emps += dept.emps
        
    def print_department(self):
        print("Parent Department")
        print(f"Base Employees: {self.base_emps}")
        print("Sub Departments:")
        for dept in self.sub_depts:
            dept.print_department()
            #print(f"{dept}: employees = {dept.emps}")
        print(f"total employees in parent department: {self.emps}")
        
dept1 = Accounting(1)
dept2 = DataScience(2)
parent_dept = ParentDepartment(30)
parent_dept.add_dept(dept1)
parent_dept.add_dept(dept2)
parent_dept.print_department()

        
