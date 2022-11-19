class student:
    __name = ""
    __totalMarks = 20

    def __init__(self, name):
        print("Run...")
        self.__name = name;
    
    def getName(self):
        print(self.__name)

    def default(self,name):
        self.__name = name

    @classmethod
    def getTotalMarks(cls):
        return student.__totalMarks

s1 = student("Bhavye")
s1.getName()
print(s1.__dict__)
s1.default("Any")
s1.getName()


# s1.__name = "Hello"
# print(s1.__name,s1.__dict__)
# s1.getName()

print(s1)
print(s1._student__name)
print(student.getTotalMarks())