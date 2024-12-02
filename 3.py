#
# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
#
#     def display_info(self):
#         print("책 제목: ", self.title)
#         print("저자: ", self.author)
#         print("가격: ", self.price)
#
#     def __eq__(self, other):
#         if isinstance(other, Book):
#             return self.price == other.price
#         return False
#
#
# book1 = Book("어린왕자", "앙투안 드 생텍쥐페리", 13000)
# book2 = Book("모모", "미하엘 엔데 저", 13000)
#
# print(book1 == book2)


class BandAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def Deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount
        else:
            print("출금 불가능")

    def display_balance(self):
        print("현재 잔액:", self.balance)


a1 = BandAccount("하이", 10000)
a1.Deposit(5000)
a1.display_balance()


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print("이름:", self.name, "/ 급여:", self.salary)


class Manager:
    def __init__(self, team_members):
        self.team_members = team_members

    def add_team_member(self, employee):
        self.team_members.append(employee)

    def display_team(self):
        print("팀원 목록:")
        for member in self.team_members:
            member.display_info()

team = []
manager = Manager(team)

employee1 = Employee("홍길동", 50000)
employee2 = Employee("김영희", 60000)

manager.add_team_member(employee1)
manager.add_team_member(employee2)
manager.display_team()
