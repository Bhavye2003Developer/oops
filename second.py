class student:
    Nameing = ""
    marks = 10

    def Name(self,name):
        student.Nameing = name
    
    def printName(self):
        print(self.Nameing)

    def increase(self):
        student.marks+=1

    def instance_increase(self):
        self.marks+=1

s1 = student()
s1.Name("Bhavye")
# s1.printName()
# print(s1.__dict__)

# s1.marks = 1
# print(s1.__dict__)

# # print(student.marks)

# s2 = student()
# print(s2.marks)
# print(s2.__dict__)

# print(s1.marks); s1.increase(); print(s1.marks);

print(s1.marks); s1.instance_increase(); print(s1.marks);

print(student.marks)