class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)
        print()
        

s1 = Student("harsha", 1, 85)
s2 = Student("tv", 2, 90)
s3 = Student("vardhan", 3, 78)

s1.display_details()
s2.display_details()
s3.display_details()
