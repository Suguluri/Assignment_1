class Calculator:
    def __init__(self):
        self.num1 = float(input("Enter the first number: "))
        self.num2 = float(input("Enter the second number: "))

    def add(self):
        return int(self.num1 + self.num2)

    def subtract(self):
        return int(self.num2 - self.num1)

    def multiply(self):
        return int(self.num1 * self.num2)

    def divide(self):
        if self.num1 == 0:
            return "Division by zero is not allowed"
        return self.num2 / self.num1


obj = Calculator()

print("Addition:", obj.add())
print("Subtraction:", obj.subtract())
print("Multiplication:", obj.multiply())
print("Division:", obj.divide())
