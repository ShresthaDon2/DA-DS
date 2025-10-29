# Magic methods are the special methods that starts and ends with __ and 
# python calls it automatically under certain situation


# __init__
# __str__
# __len__
# __add__
# __sub__
# __mul__

class Student:
    def __init__(self, name, marks, roll):
        self.name = name 
        self.marks = marks
        self.roll = roll
        # print(f"{self.name} has scored {self.marks}")
    def __str__(self):
        return f"{self.name} has scored {self.marks}" 

    
    def __len__(self,item):
        count = 0
        for i in item:
            count +=1
        return count    


s1 = Student("Ishan",45,5)
s2 = Student("Rooney",45,85)
print(s1)
print(s2)

count = len("Ishan sss")
print(count)