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
def load_trans_data():
    try:
        with open("transaction details.json", "r") as file:
            return json.load(file)
    except:
        return []
def save_trans_data(tra):
    with open("transaction details.json", "w") as file:
        json.dump(transaction_data,file,indent=4)
def save_data(data):
    try:
        with open("Account details.json","w") as file:
            json.dump(data,file,indent=4)
    except(FileNotFoundError,JSONDecodeError):
        print("Error Occurred In File Opening ")
def create_account():
    name=input("Enter Account Holder name: ")
    first_deposit=int(input("Enter Their First Deposit: "))
    account_number=acc_num_gen()
    data.append({"account_number":account_number,"name":name,"current_balance":first_deposit})
    save_data(data)
    print("Account Creation Successful")
def check_balance():
    acc_num=int(input("Enter Account Holder Number to check balance: "))
    for account in data:
        if account["account_number"]==acc_num:
            print("*"*30)
            print(f"your account name is {account['name']}")
            print(f"your current balance is {account['current_balance']}")
            print("*"*30)
            return
        print("*" * 30)
        print("No Account Found")
        print("*" * 30)
def withdraw():
    acc_num=int(input("Enter Account Holder Account Number to withdraw money:  "))
    for account in data:
        if account["account_number"]==acc_num:
            withdraw_amount=int(input("Enter the amount to withdraw: "))
            print(f"The Current Balance is {account["current_balance"]}")
            if 0 < withdraw_amount <= account["current_balance"]:
                account["current_balance"]=account["current_balance"]-withdraw_amount
                print(f"The amount of {withdraw_amount} has been credited from {account['name']} account")
                print(f"The remaining balance is {account['current_balance']}")
                save_data(data)
                #This is for transaction details
                transaction_data.append({
                    "account_number":account["account_number"],
                    "name":account["name"],
                    "type":"Withdraw",
                    "withdraw_amount":withdraw_amount,
                    "current_balance":account["current_balance"]
                })
                save_trans_data(transaction_data)
def deposit():
    acc_num=int(input("Enter Account Holder Number to Deposit number: "))
    for account in data:
        if account["account_number"]==acc_num:
            deposit_amount=int(input("Enter the Amount Depositor wants to make: "))
            if deposit_amount > 0:
                account["current_balance"]=account["current_balance"]+deposit_amount
                print(f"Amount of {deposit_amount}  has been deposited to {account["account_number"]} name {account["name"]}")
                print(f"The current balance is: {account["current_balance"]}")
                #this is for transaction details
                transaction_data.append({
                    "account_number": account["account_number"],
                    "name": account["name"],
                    "type": "Deposit",
                    "Deposit_amount": deposit_amount,
                    "current_balance": account["current_balance"]
                })
                save_trans_data(transaction_data)
def transaction_history():
    acc_num = int(input("Enter Clients Account Number to see transaction details:  "))
    for account in transaction_data:
        if account["account_number"] == acc_num:
            print(account)
def acc_num_gen():
    #This function is responsible for assigning random and unique account number to new User
    random_number=rd.randint(100000000,999999999)
    if random_number not in used_number:
        used_number.add(random_number)
    return random_number
data=load_data()
transaction_data=load_trans_data()
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


 