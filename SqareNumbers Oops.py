class Point:
    def __init__(self, x, y, z):
       
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
       
        return self.x**2 + self.y**2 + self.z**2


x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
z = float(input("Enter the value of z: "))


point = Point(x, y, z)


result = int(point.sqSum())


print(f"The sum of squares is: {result}")
