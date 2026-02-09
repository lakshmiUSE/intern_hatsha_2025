class Circle:
    def area(self):
        r = 5
        print("Area of Circle:", 3.14 * r * r)


class Rectangle:
    def area(self):
        l = 4
        b = 6
        print("Area of Rectangle:", l * b)

c = Circle()
r = Rectangle()

c.area()
r.area()
