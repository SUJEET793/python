"""
the instance variable are the variable which is changing with respect to object to object
the instance variable is defiened inside the
  1) inside the constructor using the self variable
  2) inside the instance method using the  self
  3) outside the class using self or class name but preference is given to the class name

"""
class Employee :
    def __init__(self,eno,ename,eid):
        #  inside the constructor using the self variable
        self.eno=eno
        self.ename=ename
        self.eid=eid

    def empl_designation(self,designation): # this is the instance method
        # inside the instance method using the  self
        self.designation=designation

employee=Employee(1,"sujeet",1)
employee1=Employee(2,"rajesh",3)
employee2=Employee(3,"Anjali",4)
print(employee.__dict__)#{'eno': 1, 'ename': 'sujeet', 'eid': 1}
print(employee1.__dict__) #{'eno': 2, 'ename': 'rajesh', 'eid': 3}
print(employee2.__dict__)#{'eno': 3, 'ename': 'Anjali', 'eid': 4}

employee1.empl_designation("CEO")
employee.empl_designation("MANAGER")
employee2.empl_designation("labour")

print(employee.__dict__)#{'eno': 1, 'ename': 'sujeet', 'eid': 1, 'designation': 'MANAGER'}
print(employee1.__dict__) #{'eno': 2, 'ename': 'rajesh', 'eid': 3, 'designation': 'CEO'}
print(employee2.__dict__)#{'eno': 3, 'ename': 'Anjali', 'eid': 4, 'designation': 'labour'}

#outside the class using object  preference variable of the class
employee.salary=100
employee2.salary=200
employee1.salary=300

print(employee.__dict__)#{'eno': 1, 'ename': 'sujeet', 'eid': 1, 'designation': 'MANAGER', 'salary': 100}
print(employee1.__dict__) #{'eno': 2, 'ename': 'rajesh', 'eid': 3, 'designation': 'CEO', 'salary': 300}
print(employee2.__dict__)#{'eno': 3, 'ename': 'Anjali', 'eid': 4, 'designation': 'labour', 'salary': 200}


