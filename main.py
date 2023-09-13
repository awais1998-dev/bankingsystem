
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_user_details(self):
        print("User Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)


class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Account balance has been updated : $", self.balance)

    def withdraw(self, amount):
        if(amount <= self.balance):
            self.balance = self.balance - amount
            print("Account balance has been updated : $", self.balance)
        else:
            print("Insufficient funds | Balance available : $", self.balance)

    def view_balance(self):
        # self.show_user_details()
        print("Your account balance is : $", self.balance)


awais = Bank("Awais", 25, "M")
awais.view_balance()
awais.deposit(500)
awais.view_balance()
awais.withdraw(500)
awais.view_balance()
