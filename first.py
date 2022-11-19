class student:
    #Attributes
    totalStudents = 30
    TeacherName = "The God"

    #Methods
    def testing(self):
        print("Testing...")
        print(self)

    def printing(self, var):
        print("Your string : " , var)

    def printName(self):
        print(self.name)



s1 = student()
s1.name = "Bhavye"  #Instance attribute
s1.age = 19

s1.totalStudents = 25
# print(s1.__dict__)

student.totalMarks = 100

# print(student.__dict__)

# print(s1.totalMarks)

# print(s1.testing())
# s1.printing("Bhavye the god")

# student.testing(s1)
# s1.printName()