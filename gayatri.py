class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):  #argument
        self.name = aname      #instance variable
        self.salary = asalary
        self.role = arole

    def printdetails(self):   #Self means the object which we are talking
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
feroz = Employee("Feroz", 255, "Instructor")
print(feroz.salary)