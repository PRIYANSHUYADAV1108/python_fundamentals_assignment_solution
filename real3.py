class student:
    def __init__(self,name, roll_number,marks):
        self._name = name
        self._roll_number = roll_number
        self._marks = marks

    def get_name(self):
       return self._name
    def set_name(self,name):
       if name == "":
          print("name cannot be empty:")
       else:
           self._name = name


    def get_roll_number(self):
       return self._roll_number
    def set_roll_number(self,roll_number):
       if 1 > roll_number and roll_number > 100 :
           print("roll number must be in between 1 and 100")
       else:
           return self._roll_number == roll_number

    def get_marks(self):
       return self._marks
    def set_marks(self,marks):
       if marks < 0:
          print("marks cannot be 0")
       else:
           self._marks = marks

stu1 = student("priyanshu",32,90)

print("name = ",stu1.get_name())
print("roll number = ", stu1.get_roll_number())
print("marks = ", stu1.get_marks())

stu1.set_roll_number(30)
stu1.set_marks(95)
stu1.set_name("priya")
print("updated marks = ", stu1.get_marks())
print("updated roll number = ",stu1.get_roll_number())


print("updated name = ", stu1.get_name())
