import time
import os
import json

#make a Banking system manager
'''===== BANK =====

1. Login
2. Create Account
3. Exit

> 1

Account Number:
Password:

Welcome John!

1. Deposit
2. Withdraw
3. Transfer
4. History
5. Logout'''

account_file = r'C:\Users\RIO SANTINO\python code files\Python beginner projects\Bank manager\data\Bank_accounts.txt'
class Bank:
    def __init__(self):
        self.current_user = None
        self.money = 0

    def create(self):
        os.system('cls')
        print('''Create Account:
---------------''')
        # open the accounts file (r+: means able to read adn write)
        with open(account_file, "r+") as file:
            accounts = json.load(file)

        #ask the user for the account they want to create
        username = input("Username: ")

        #check if username already exists
        if username in (accounts):
            print("Username already exists: Try again")
            return

        password = input('password: ')

        #format of how the text will be written in the file
        accounts[username] = {
        
                "password": password,
                "balance": 1500
            }
        
        #put the formatted data in file
        with open(account_file, "r+") as file:
            json.dump(accounts, file, indent=4)
            

       
    def login(self):
        os.system('cls')
        print('=====LOGIN====')
        with open(account_file, "r+") as Bank_Usernames:
            accounts = json.load(Bank_Usernames)
            print(accounts)

            #ask for username
            username = input('Username: ')

            #check if the Account exists
            if username in (accounts):
                password = input("Password: ")

                #Check if password is correct
                if password == accounts[username]['password']:
                    print('login success')
                    self.current_user = username
                    self.user_menu()
                    

                elif password != accounts[username]['password']:
                    print('wrong password')
                    #attempts +=1 


            else:
                print('Account does not exist, Try Again')

    def start_menu(self):
        os.system('cls')
        #starting values
        attempts = 0
        choice = ''

        print("welcome to World bank What would you like to do?")

        while choice not in (1,2,3):
            choice = input('''===== BANK =====
    1. Login
    2. Create Account
    3. Exit
    -----------------
    > ''')

            if choice == '1':
                self.login()

            elif choice == '2':
                self.create()

            elif choice == "3":
                with open(account_file, "r") as file:
                    accounts = json.load(file)
                    print(os.getcwd())
                    print(accounts)
                    print(Bank.current_user)
                    
            else:
                print("Try again, Unrecognized Input")

        return



    #user menu options
    def deposit(self):
        with open(account_file, "r+") as Bank_Usernames:
            accounts = json.load(Bank_Usernames)
            print(f"Balance: {accounts[self.current_user]['balance']} PHP")

        deposit = float(input("Deposit: PHP "))
        os.system('cls')
       
        try:
            accounts[self.current_user]['balance'] += deposit 

            with open(account_file, "r+") as file:
                json.dump(accounts, file, indent=4)

        except:
            print("invalid ammount")

        

    def withdraw(self):
        with open(account_file, "r+") as Bank_Usernames:
            accounts = json.load(Bank_Usernames)
            print(f"Balance: {accounts[self.current_user]['balance']}")
        
        withdraw = float(input("Withdraw: Php "))
        os.system('cls')
      
        #valid check of withdraw ammount
        if withdraw <= accounts[self.current_user]['balance']:
            accounts[self.current_user]['balance'] -= withdraw 
                    
            with open(account_file, "r+") as file:
                json.dump(accounts, file, indent=4)
            
        else:
            print("invalid ammount")
           

    def transfer(self):
        print("====TRANSFER====")
        with open(account_file, "r+") as Bank_Usernames:
            accounts = json.load(Bank_Usernames)
            print(f"Balance: {accounts[self.current_user]['balance']}")
                
            #ask for account to tranfer and amount
            account = input("Account: ")
            #account check
            if account not in (accounts):
                print("invalid account")
                return

            
            amount = input("Amount: ")

            #check if amount is valid
            try:
                amount = float(amount)
            except ValueError:
                print("invalid int")
                return

            if float(amount) >= 0:
                print(f" {accounts[account]}: {accounts[account]['balance']} PHP")
                confirm = input("enter amount again to confirm: ")

                try:
                    confirm = float(confirm)
                except ValueError:
                    print("invalid amount")
                    return

                if confirm == amount:
                    accounts[self.current_user]["balance"] -= amount
                    accounts[account]['balance'] += amount

                    print(f"Balance: {accounts[self.current_user]['balance']}")

                    with open(account_file, "r+") as file:
                        json.dump(accounts, file, indent=4)
                    

            else:
                print("invalid amount")

            

        

    def history(self):
        ...
    def logout(self):
        self.current_user = None
        print("Logout")
    

    def user_menu(self):
        os.system('cls')
        choice = ''

        while choice != ("5"):
            print(f"======= Welcome {self.current_user} =======")
            with open(account_file, "r+") as Bank_Usernames:
                accounts = json.load(Bank_Usernames)
                print(f"Balance: {accounts[self.current_user]['balance']}")

        
            choice = input('''
    1. Deposit
    2. Withdraw
    3. Transfer            
    4. History
    5. Logout
    -----------------
    > ''')

            if choice == '1':
                self.deposit()

            elif choice == "2":
                self.withdraw()

            elif choice == "3":
                self.transfer()

            elif choice == "4":
                self.history()

            elif choice == "5":
                self.logout()
            else:
                print('test')

    
    


        
def __main__():
    bank = Bank()
    while bank.current_user == None:
        bank.start_menu()


__main__()