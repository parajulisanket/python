# Design a bank class
# open an account(fn, ln , age, balance= 0)
# get current balance
# deposit balance
# withdraw balance
# get interest rate(12%)
# print government holidays

class Bank:
    Interest = '12%'
    def _init_(self, first_name, last_name, age, initial_balance):
        self.customers = {}   
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.initial_balance = initial_balance
        self.full_name = self.first_name + ' ' + self.last_name
        self.full_details = [self.first_name + ' '+ self.last_name , self.age]

    def open_account(self):
        print("Starting the process to open your account----->")
        
        print(f"Congratulations {self.first_name} , you have opened your new account!")
        self.customers['details'] = self.full_details
        # print(self.full_details)
        # print(self.Interest)
        
    def get_current_balance(self):
        print(f"Dear {self.full_name}, your current balance is {self.initial_balance} ")
        
    def deposit_balance(self, deposit_balance):
        self.initial_balance = self.initial_balance + deposit_balance
        print(f"Your balance has been deposited and your new balance is {self.initial_balance}")
        
    def withdraw_balance(self, withdraw_balance):
        if withdraw_balance <= self.initial_balance:
            self.initial_balance = self.initial_balance - withdraw_balance
        else:
            print("Sorry, your account doesn't have enough balance.")
    @classmethod
    def get_interest(self):
        print(f"Interest rate is {Bank.Interest}")

    def holidays(self):
        pass
        


while True:      
    print("Welcome to Your Bank")
    print("------- Dashboard --------")
    print("Chose one of these operations:(1-7) ")
    print("1. Open an account.")
    print("2. Get current balance.")
    print("3. Deposit balance.")
    print("4. Withdraw balance.")
    print("5. Interest Rate")
    print("6. Public Holiday.")
    operation = int(input("Enter your option: "))

    
    
    if operation == 1:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        age = int(input("Enter your age : "))
        initial_balance = int(input("Enter your initial balance: "))
        person1 = Bank(first_name, last_name, age, initial_balance)
        person1.open_account()

    elif operation == 2:
        person1.get_current_balance()
    elif operation == 3:
        deposit_balance = int(input("Enter the balance you want to deposit: "))
        person1.deposit_balance(deposit_balance)
    elif operation == 4:
        withdraw_balance = int(input("Enter the balance you want to withdraw: "))
        person1.withdraw_balance(withdraw_balance)
    elif operation == 5:
        Bank.get_interest()
    elif operation == 5:
        pass

    