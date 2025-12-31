import random as rd
import json as json
from json import JSONDecodeError
used_number = set()
def load_data():
    try:
        with open("Account details.json","r") as file:
            return json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        return []

def save_data(data):
    try:
        with open("Account details.json","w") as file:
            json.dump(data,file)
    except(FileNotFoundError,JSONDecodeError):
        print("Error Occurred In File Opening ")
def create_account():
    name=input("Enter Account Holder name: ")
    first_deposit=input("Enter Their First Deposit: ")
    account_number=acc_num_gen()
    data.append({"account_number":account_number,"name":name,"current_balance":first_deposit})
    save_data(data)
    print("Account Creation Successful")
def check_balance():
    check_balance_acc_num=int(input("Enter Account Holder Name to check balance: "))
    for account in data:
        if account["account_number"]==check_balance_acc_num:
            print("*"*30)
            print(f"your account name is {account['name']}")
            print(f"your current balance is {account['current_balance']}")
            print("*"*30)
            return
        print("*" * 30)
        print("No Account Found")
        print("*" * 30)

def withdraw():
    pass
def deposit():
    pass
def transaction_history():
    pass
def acc_num_gen():
    random_number=rd.randint(100000000,999999999)
    if random_number not in used_number:
        used_number.add(random_number)
    return random_number
data=load_data()
def main():
    while True:
        print("Welcome to Islamic Bank")
        print("Select the service you want to avail")
        print("1. Create Account")
        print("2. Check Account Balance")
        print("3. Withdraw Money")
        print("4. Deposit Money")
        print("5. View Transaction History")
        choice=input("Enter Service Number: ")

        match choice:
            case "1":
                create_account()
            case "2":
                check_balance()
            case "3":
                withdraw()
            case "4":
                deposit()
            case "5":
                transaction_history()

            case _:
                print("Invalid choice")
                return
if __name__=="__main__":
    main()
