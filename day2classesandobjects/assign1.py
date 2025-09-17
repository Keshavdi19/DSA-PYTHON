# class Test:
#     x = 5
#     def f1():
#         print("hello")
# t1 = Test()
# t2 = Test() #instance object,# class objest is only test
# one class have only one class opbject but it can have more than one number of instance objects
# class Test:
#     def __init__(self):
#         self.a = 5
#         self.b = 6
# t1 = Test()
# t2 = Test()
# print(t1.a,t1.b)
# print(t2.a,t2.b)
class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
t1 = Test(3,4)
t2 = Test(5,6)
print(t1.a,t1.b)
print(t2.a,t2.b)
# instance,class,and static methods are
class Triangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    def show(self):
        print(self.a, self.b)
    def f1(self):
        pass
    @staticmethod
    def f2():
        print("Hello")
    @classmethod
    def f3(cls):
        print(cls.x)
t1 = Triangle(3,4)
t2 = Triangle(5,6)
t1.show()
t2.show()
Triangle.f3()
Triangle.f2()









