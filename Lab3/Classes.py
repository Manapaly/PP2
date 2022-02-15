class Strings:
    def __init__(self,name):
        self.name = name
    def get_string(self):
        return self.name
    def print_string(self):
        print(self.name.upper())
# S1 = Strings('ernat')
# print(S1.get_string())
# S1.print_string()


class Shape:
    def __init__(self,name):
        self.area = name
    def area0(self):
        print(0)

class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side
    def area1(self):
        print(self.side*self.side)

class Rectangle(Shape):
    def __init__(self, name, a_side, b_side):
        super().__init__(name)
        self.a_side = a_side
        self.b_side = b_side
    def area2(self):
        print(self.a_side * self.b_side)
# F1 = Shape('фигура')
# F2 = Square('төртбұрыш', 4)
# F3 = Rectangle('тиктортбурыш', 4, 5)
# F2.area1()
# F3.area2()

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(f'{self.x},{self.y}')
    def move(self,x1,y1):
        self.x = x1
        self.y = y1
    def dist(self,point2):
        res = ((self.x - point2.x)**2 + (self.y - point2.y)**2)**0.5
        print(res)
# p1 = Point(123,1324)
# p2 = Point(3,4)
# p1.show()
# p1.move(0,0)
# p1.dist(p2)

class Account:
    def __init__(self, name, soname, balance):
        self.name = name
        self.soname = soname
        self.balance = balance
    def deposit(self, money):
        self.balance = self.balance + money
    def withdraw(self, unmoney):
        if self.balance - unmoney < 0: print('Недостаточно средств для снятия')
        else: self.balance = self.balance - unmoney
    def show_balance(self):
        print(self.balance)
# A = Account('Ернат', "Манапалы", 31000)
# A.deposit(31000)
# A.show_balance()
# A.withdraw(60000)
# A.show_balance()
# A.withdraw(4000)