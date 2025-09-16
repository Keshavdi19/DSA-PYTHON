class Employee:
    def __init__(self, Empid = None, Name = None, salary = None):
        self.Empid = Empid
        self.Name = Name
        self.salary = salary
    def setEmpid(self, Empid):
        self.Empid = Empid
    def setName(self, name):
        self.name = name
    def setSalary(self, salary):
        self.salary = salary
    def getEmpid(self):
        return self.Empid
    def getName(self):
        return self.Name
    def getSalary(self):
        return self.salary
e1 = Employee()
e2 = Employee(2, "keshav", 100000)
e1.setEmpid(2)
e1.setName("madhav")
e1.setSalary(2399939)
print(e1.getEmpid(),e1.getName(),e1.getSalary())
print(e2.getEmpid(),e2.getName(),e2.getSalary())