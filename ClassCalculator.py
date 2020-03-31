class calculator():

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def addition(self):
        result = self.first + self.second
        print(result)

    def subtraction(self):
        result = self.first - self.second
        print(result)

    def multiplication(self):
        result = self.first * self.second
        print(result)

    def division(self):
        result = self.first / self.second
        print(result)


Cal1 = calculator(2, 3)
Cal1.addition()

Cal2 = calculator(4, 9)
Cal2.subtraction()

Cal3 = calculator(7, 8)
Cal3.multiplication()

Cal4 = calculator(9, 3)
Cal4.division()
