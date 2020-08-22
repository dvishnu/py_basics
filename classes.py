# basics on python classes

# __init_() is always executed when a class is being initiated

class student:
    def __init__(self,name,age):
        self.name = name # self reference
        self.age = age
        print("Hi My name is {} and i am {} years old".format(name,age))
s1 = student("Vishnu", 28)

print("My age is {}".format(s1.age))
print("My name  is {}".format(s1.name))

# classes with methods
#
# class emp:
#     def __init__(self,empid,dept):
#         self.empid = empid
#         self.dept = dept
#     def dept_name(self):
#         if self.dept == '10':
#             print("dept name is Sales")
#         elif self.dept == '20':
#             print("dept name is Accounts")
#         else:
#             print("emp belongs to unknown department")
# e1 = emp(1,10)
#
#
# # calling the methods in the class from the object created
# e1.dept_name()


class student1:
    def __init__(self,name,section,school):
        self.name = name
        self.section = section
        self.school = school
    def std_details(self):
        print("student name from student details method is {} ".format(self.name))
s2 = student1("robo","A","loyolla")

s2.std_details()

# Inheritance classes

class car:
    def __init__(self,car_name,model):
        self.car_name = car_name
        self.model = model
    def car_details(self):
        print("Car name is {} and model is {}".format(self.car_name,self.model))

c = car("hyundai","nios")
# calling the car details method
c.car_details()

Now defining Child class

class maruti(car):
    def __init__(self,car_name,model): # init fun overrides the init def from the parent class

        super().__init__(car_name, model)
        self.car_color = "blue"
        print("Inherited props i.e car name is {} and model is {}".format(car_name,model))
c2 = maruti("mar","baleno")
print(c2.car_color)
