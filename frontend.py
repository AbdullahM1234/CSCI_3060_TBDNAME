# Basic front end skeleton structure

# Group members
# Samir Neogi - 100923675
# Abdullah Mobashar - 100918452 
# Megan Brandreth - 100778693
# Brian Husted - 100878395

import os 

name = "u"  # default name (means not logged in)
session = "standard"  # default session

accounts = {}  # stores all accounts loaded from file
session_transactions = []  # stores transactions during current session

# make sure you run the py file in the CSCI_3060_TBDNAME directory
# or the file reading wont work
ACCOUNTS_FILE = "accounts.txt"
DAILY_TX_FILE = "transactions/daily_transactions.txt"

VALID_PAYEES = [  # allowed payees for paybill
    "Company",
    "Business Inc",
    "John Business",
]


def load_accounts():
    # loads account data from accounts.txt into memory
    global accounts
    accounts = {}

    f = open(ACCOUNTS_FILE, "r", encoding="utf-8")  # open accounts file
    for raw in f:
        line = raw.strip()  # remove whitespace
        if line == "":
            continue  # skip empty lines

        parts = line.split()  # split line into fields
        acc_name = parts[0]
        acc_num = parts[1]
        bal = float(parts[2])
        status = parts[3]
        plan = parts[4]

        accounts[acc_num] = {  # store account info in dictionary
            "name": acc_name,
            "balance": bal,
            "status": status,
            "plan": plan
        }
    f.close() 


def write_daily_transactions():
    # writes all session transactions to file and adds 00 at end
    global session_transactions

    f = open(DAILY_TX_FILE, "w", encoding="utf-8")  # open output file
    for rec in session_transactions:
        f.write(rec + "\n")  # write each transaction
    f.write("00\n")  # end of session record
    f.close()


def login():
    # handles login for admin or standard session
    global name, session

    if name != "u":  # check if already logged in
        print("You are already logged in.")
        session_transactions.append("01 LOGIN STANDARD " + acc_num + " " + name + " FAIL_LOGGED_IN")
        return

    print("Welcome.")
    print("What session are you opening today? (admin or standard)")
    sessionType = input().strip().lower()

    if sessionType == "admin":
        print("admin selected.")
        session = "admin"
        name = "admin"
        session_transactions.append("01 LOGIN ADMIN")  # record login
        return

    print("standard selected.")
    session = "standard"

    acc_num = input("Account number: ").strip()
    if acc_num not in accounts:
        print("Account does not exist.")
        session_transactions.append("01 LOGIN STANDARD " + acc_num + " " + name + " FAIL_ACCOUNT_NUMBER_DNE")
        return

    if accounts[acc_num]["status"].upper() == "D":
        print("Account is disabled.")
        session_transactions.append("01 LOGIN STANDARD " + acc_num + " " + name + " FAIL_ACCOUNT_DISABLED")
        return
    

    name = accounts[acc_num]["name"]
    session_transactions.append("01 LOGIN STANDARD " + acc_num + " " + name)
    print("Welcome, " + name + ".")
    return


def logout():
    # ends session and writes transaction file
    global name, session, session_transactions

    if name == "u":  # check if logged in
        print("You are not logged in.")
        return

    write_daily_transactions()  # write session transactions

    name = "u"  # reset login
    session = "standard"
    session_transactions = []

    print("Logged out.")
    return


def withdrawal():
    # handles withdrawal transaction
    global name, session

    if name == "u":  # must be logged in
        print("You are not logged in.")
        session_transactions.append("02 WITHDRAW FAIL_NO_LOGIN")
        return

    if session == "admin":
        accountName = input("Account holder name: ").strip()
    else:
        accountName = name

    accountNum = input("Account number: ").strip()
    withdraw_amt = float(input("Withdrawal amount: ").strip())

    if withdraw_amt > 500:  # check limit
        print("Exceeds withdraw limit.")
        session_transactions.append("02 WITHDRAW " + accountNum + " " + str(withdraw_amt) + " " + accountName + " FAIL_EXCEEDS_SESSION_LIMIT")
        return

    if accountNum not in accounts:
        print("Account does not exist.")
        session_transactions.append("02 WITHDRAW " + accountNum + " " + str(withdraw_amt) + " " + accountName + " FAIL_INVALID_ACCOUNT_NUM")
        return

    if accounts[accountNum]["status"].upper() == "D":
        print("Account is disabled.")
        session_transactions.append("02 WITHDRAW " + accountNum + " " + str(withdraw_amt) + " " + accountName + " FAIL_ACCOUNT_DISABLED")
        return

    # missing overdraft case

    # missing deleted account case

    accounts[accountNum]["balance"] = accounts[accountNum]["balance"] - withdraw_amt
    session_transactions.append("02 WITHDRAW " + accountNum + " " + str(withdraw_amt) + " " + accountName)
    print("Withdrawal recorded.")
    return


def transfer():
    # handles transfer transaction
    global name, session

    if name == "u":
        print("You are not logged in.")
        session_transactions.append("03 TRANSFER FAIL_NO_LOGIN")
        return

    if session == "admin":
        accountName = input("Account holder name: ").strip()
    else:
        accountName = name

    acc1 = input("From account number: ").strip()
    acc2 = input("To account number: ").strip()
    transferAmount = float(input("Transfer amount: ").strip())

    if transferAmount > 1000:  # check limit
        print("Exceeds transfer limit.")
        session_transactions.append("03 TRANSFER " + acc1 + " " + acc2 + " " + str(transferAmount) + " " + accountName + " FAIL_LIMIT_EXCEEDED")
        return

    if acc1 not in accounts or acc2 not in accounts:
        print("One of the accounts does not exist.")
        session_transactions.append("03 TRANSFER " + acc1 + " " + acc2 + " " + str(transferAmount) + " " + accountName + " FAIL_INVALID_RECIPENT")
        return

    if accounts[acc1]["status"].upper() == "D" or accounts[acc2]["status"].upper() == "D":
        print("One of the accounts is disabled.")
        session_transactions.append("03 TRANSFER " + acc1 + " " + acc2 + " " + str(transferAmount) + " " + accountName + " FAIL_ACCOUNT_DISABLED")
        return
    
    # missing overdraft test case

    # missing deleted account case

    accounts[acc1]["balance"] = accounts[acc1]["balance"] - transferAmount
    accounts[acc2]["balance"] = accounts[acc2]["balance"] + transferAmount

    session_transactions.append("03 TRANSFER " + acc1 + " " + acc2 + " " + str(transferAmount) + " " + accountName)
    print("Transfer recorded.")
    return


def paybill():
    # handles paybill transaction
    global name, session

    if name == "u":
        print("You are not logged in.")
        session_transactions.append("04 PAYBILL FAIL_NO_LOGIN")
        return

    if session == "admin":
        accountName = input("Account holder name: ").strip()
    else:
        accountName = name

    accNum = input("Account number: ").strip()
    payee = input("Payee: ").strip()
    billPaid = float(input("Bill amount: ").strip())

    if billPaid > 2000:  # check limit
        print("Exceeds bill limit.")
        session_transactions.append("04 PAYBILL " + accNum + " " + str(billPaid) + " " + payee + " " + accountName + " FAIL_EXCEEDS_SESSION_LIMIT")
        return

    if accNum not in accounts:
        print("Account does not exist.")
        session_transactions.append("04 PAYBILL " + accNum + " " + str(billPaid) + " " + payee + " " + accountName + " FAIL_ACCOUNT_NUM_DNE")
        return

    if payee not in VALID_PAYEES:
        print("Payee invalid.")
        session_transactions.append("04 PAYBILL " + accNum + " " + str(billPaid) + " " + payee + " " + accountName + " FAIL_INVALID_PAYEE")
        return
    
    # missing overdraft case

    # missing invalid account name case

    # missing deleted account case

    # missing disabled account case

    accounts[accNum]["balance"] = accounts[accNum]["balance"] - billPaid
    session_transactions.append("04 PAYBILL " + accNum + " " + str(billPaid) + " " + payee + " " + accountName)
    print("Bill payment recorded.")
    return


def deposit():
    # handles deposit transaction
    global name, session

    if name == "u":
        print("You are not logged in.")
        session_transactions.append("05 DEPOSIT FAIL_NO_LOGIN")
        return

    if session == "admin":
        accountName = input("Account holder name: ").strip()
    else:
        accountName = name

    accNum = input("Account number: ").strip()
    amount = float(input("Deposit amount: ").strip())

    if accNum not in accounts:
        print("Account does not exist.")
        session_transactions.append("05 DEPOSIT " + accNum + " " + str(amount) + " " + accountName + " FAIL_INVALID_ACCOUNT_NUMBER")
        return
    
    # missing disabled account case

    # missing deleted account case

    accounts[accNum]["balance"] = accounts[accNum]["balance"] + amount
    session_transactions.append("05 DEPOSIT " + accNum + " " + str(amount) + " " + accountName)
    print("Deposit recorded.")
    return


def create():
    # creates new account (admin only)
    global name, session

    if name == "u":
        print("You are not logged in.")
        session_transactions.append("06 CREATE FAIL_NO_LOGIN")
        return

    if session != "admin":
        print("Admin only.")
        session_transactions.append("06 CREATE FAIL_ADMIN_ONLY")
        return

    accountName = input("Account holder name: ").strip()
    balanceinit = float(input("Initial balance: ").strip())

    new_num = "10000"
    while new_num in accounts:
        new_num = str(int(new_num) + 1)

    accounts[new_num] = {
        "name": accountName,
        "balance": balanceinit,
        "status": "A",
        "plan": "N"
    }

    # missing name too long case

    # missing too much money case

    # missing non-unique case

    session_transactions.append("06 CREATE " + new_num + " " + accountName + " " + str(balanceinit))
    print("Account created: " + new_num)
    return


def delete():
    # deletes account (admin only)
    global name, session

    if name == "u":
        print("You are not logged in.")
        session_transactions.append("07 DELETE FAIL_NO_LOGIN")
        return

    if session != "admin":
        print("Admin only.")
        session_transactions.append("07 DELETE FAIL_NOT_ADMIN")
        return

    accountName = input("Account holder name: ").strip()
    accNum = input("Account number: ").strip()

    if accNum not in accounts:
        print("Account does not exist.")
        session_transactions.append("07 DELETE " + accNum + " " + accountName + " FAIL_NO_MATCH")
        return

    # missing text case for name not matching

    del accounts[accNum]
    session_transactions.append("07 DELETE " + accNum + " " + accountName)
    print("Account deleted.")
    return


def disable():
    # disables account (admin only)
    global name, session

    if name == "u":
        print("You are not logged in.")
        session_transactions.append("08 DISABLE FAIL_NO_LOGIN")
        return

    if session != "admin":
        print("Admin only.")
        session_transactions.append("08 DISABLE FAIL_NOT_ADMIN")
        return

    accountName = input("Account holder name: ").strip()
    accNum = input("Account number: ").strip()

    if accNum not in accounts:
        print("Account does not exist.")
        session_transactions.append("08 DISABLE " + accNum + " " + accountName + " FAIL_NUMBER_DNE")
        return
    
    # missing name not matching case

    accounts[accNum]["status"] = "D"
    session_transactions.append("08 DISABLE " + accNum + " " + accountName)
    print("Account disabled.")
    return


def changeplan():
    # toggles account plan (admin only)
    global name, session

    if name == "u":
        print("You are not logged in.")
        session_transactions.append("09 CHANGEPLAN FAIL_NO_LOGIN")
        return

    if session != "admin":
        print("Admin only.")
        session_transactions.append("09 CHANGEPLAN FAIL_NOT_ADMIN")
        return

    accountName = input("Account holder name: ").strip()
    accNum = input("Account number: ").strip()

    if accNum not in accounts:
        print("Account does not exist.")
        session_transactions.append("09 CHANGEPLAN " + accNum + " " + accountName + " FAIL_MISMATCH")
        return
    
    # missing deleted account case

    current = accounts[accNum]["plan"].upper()
    if current == "S":
        accounts[accNum]["plan"] = "N"
    else:
        accounts[accNum]["plan"] = "S"

    session_transactions.append("09 CHANGEPLAN " + accNum + " " + accountName)
    print("Plan changed.")
    return


def main():
    # main menu loop
    load_accounts()

    while True:
        print("\nWelcome! What would you like to do?\n")
        print("1. Log in")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Pay Bill")
        print("5. Deposit")
        print("6. Create Account")
        print("7. Delete Account")
        print("8. Disable Account")
        print("9. Change Account Plan")
        print("10. Log Out")
        print("11. Exit\n")

        choice = input("Please input the number of your selection to be redirected: ").strip()

        match choice:
            case "1":
                login()
            case "2":
                withdrawal()
            case "3":
                transfer()
            case "4":
                paybill()
            case "5":
                deposit()
            case "6":
                create()
            case "7":
                delete()
            case "8":
                disable()
            case "9":
                changeplan()
            case "10":
                logout()
            case "11":
                print("Goodbye.")
                break
            case _:
                print("Unknown operation. Please try again.")


if __name__ == "__main__":
    main()