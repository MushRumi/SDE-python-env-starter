class Subtraction:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def subtract(self):
        return self.num1 - self.num2

problem = Subtraction(1123120, 5)
print(problem.subtract())


class Book:
    def __int__(self, title, author, year)