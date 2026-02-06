# global variables
name = "u" # default name
session = "standard" # default session


def login():

    # check if user has already logged in
    # i.e if username does not equal u

    # if user is logged in, error message and redirect to log out
    if username == "u":
        print("You are already logged in. Logout?")
        logAns = input("(y/n): ")
        if logAns == "y" or logAns == "Y":
            logout()
        else:
            return
    
    # else
    print("Welcome.")
    print("What session are you opening today? (admin or standard)\n")
    sessionType = input()

    if sessionType == "admin":
        print("admin selected.")
        session = "admin"

        # do not prompt for name input, move straight to menu
        return

    else:
        print("standard selected.")
        name = input("Name: ") 
        # existing & valid account check

        # if not valid or not existing, prompt to create a new account or try again
        """
        
        print("Account does not exist or credentials were invalid.\n")

        # reset username to default
        username = "username"

        print("press button to try again")
        loginDecision = input()
        login()

        """

        print(f"Welcome, {name}.")

        # print account details

    return

def logout():
    # check that user is logged in (username not default)

    if name == "u":
        print("You are not logged in.")
        return
    
    # print transactions made during session

    # check for deposited money during session, add that to usable account funds

    # set account to available for transactions

    # reset name and session to default (not logged in)

    # log back in once logged out
    login()

def withdrawal():
    # check session and check login

    if name == "u":
        print("You are not logged in.")
        return
    
    # check if available for transactions
        # if not, prompt to log out 

    # if admin, ask for account holder name
    if session == "admin":
        print("Please provide the account holder's name.")
        accountName = input()
    else:
        accountName = name
    # check that account name is valid
        # if not, prompt to try again

    # ask for account number
    print("Please provide the account number.")
    accountNum = input()
    # check account number is valid
        # if not, prompt to try again
    # check if account number is associated with account name
        # if not, return

    # ask for  withdrawal amount
    print("Please enter the withdrawal amount.")
    withdraw = input()

    # check if more than $500
    if withdraw >= 500:
        #if true, prompt to try again
        print("Sorry, this exceeds our withdraw limit of 500.\n Please try again.")
        withdrawal()
    
    # check that bank account will have at least $0 after transaction
        # if either true, reject withdrawal, return to menu

    # save to bank transaction file

    return

def transfer():
    # check session and check login

    if name == "u":
        print("You are not logged in.")
        return

    # check if available for transactions
        # if not, prompt to log out 

    # if admin, ask for account holder name
    if session == "admin":
        print("Please provide the account holder's name.")
        accountName = input()
    else:
        accountName = name
    # check that account name is valid
    # if not, prompt to try again

    # ask for account number 1
    print("Please provide the number for the account you are transfering from.")
    acc1 = input()
    # check if valid
        # if not, prompt to try again

    # ask for account number 2
    print("Please provide the number of the account you are transfering to.")
    acc2 = input()
    # check if valid
        # if not, prompt to try again 

    # ask for transfer ammount
    print("please provide a transfer amount.")
    transferAmount = input()

    # check if more than $1000
    if transferAmount >= 1000:
        #if true, prompt to try again
        print("Sorry, this exceeds our withdraw limit of 500.\n Please try again.")
        transfer()
    # check if back account 1 will have at least $0 after transfer
    # check that account 2 is not overdrafted
        # if any true, reject transfer, return to menu

    # save to bank transaction file

    return

def paybill():
    # check session and check login

    if name == "u":
        print("You are not logged in.")
        return

    # check if available for transactions
        # if not, prompt to log out 

    # if admin, ask for account holder name
    if session == "admin":
        print("Please provide the account holder's name.")
        accountName = input()
    else:
        accountName = name

    # ask for account number
    print("Please provide an account number.")
    accNum = input()
    # check if valid
        # if not, prompt to try again

    # ask for payee
    print("Please provide the name of the Payee.")
    payee = input()
    # check if valid payee
    if payee != "The Bright Light Electric Company (EC)" or "Credit Card Company Q (CQ)" or "Fast Internet, Inc. (FI)":
        # if not, prompt to try again
        print("Payee invalid. Try again.")
        paybill()

    # ask for bill pay amount
    print("Please enter the amount to be paid.")
    billPaid = input()

    # check if more than $2000
    if billPaid >= 2000:
        print("This payment exceeds our payment limit. Please try again.")
        paybill()
    # check if account will have at least $0 after payment
        # if either, reject payment and return to menu

    # save to bank transaction file

    return


def deposit():
    # check session and check login

    if name == "u":
        print("You are not logged in.")
        return

    # check if available for transactions
        # if not, prompt to log out 

    # if admin, ask for account holder name
    if session == "admin":
        print("Please provide the account holder's name.")
        accountName = input()
    else:
        accountName = name

    # ask for account number
    print("Please provide an account number.")
    accNum = input()
    # check if valid
        # if not, prompt to try again
    
    # ask for deposit amount
    print("Please provide the amount to be deposited.")
    deposit = input()

    # save to bank transaction file

    # store to be added at end of session

    return

def create():
    # check session type, only accept if admin

    if name == "u":
        print("You are not logged in.")
        return 
    # ask for name
    if session == "admin":
        print("Please provide the account holder's name.")
        accountName = input()
        # check if exists
            # if it does, prompt to try again
        # check if name is more than 20 characters
        if len(accountName) > 20:
            # if it is, prompt to try again
            print("Name provided is too long. Try again.")
            create()
            

        # ask for inital account balance
        print("Please provide initial account balance.")
        balanceinit = input()
        # check if less than $99999.99
        if balanceinit >= 100000:
            # if not, prompt to try again
            print("Balance exceeds limit. Please try again.")
            create()

        # generate random account number

        # save and print info to bank transaction file

        # note to not allow transactions on this account until session ends
        # else, return
    else:
        return
    return

def delete():
    # check session type, only accept if admin

    if session == "admin":
        # ask for name
        print("Please provide the account holder's name.")
        accountName = input()
        # check if exists
            # if not, prompt to try again
            
        # ask for account number
        print("Please provide an account number.")
        accNum = input()
        # check if exists
            # if not, prompt to try again
        # check if associated with name
            # if not, return to menu
            
        # save to bank transaction file

        # set data to deleted
    # else, return
    else:
        return
    return

def disable():
    # check session type, only accept if admin
    if session == "admin":
    # ask for name
        print("Please provide the account holder's name.")
        accountName = input()
        # check if exists
            # if not, prompt to try again

        # ask for account number
        print("Please provide an account number.")
        accNum = input()
        # check if exists
            # if not, prompt to try again
        # check if associated with name
            # if not, return to menu
            
        # change bank account status to disabled and no transactions
        # save to bank account transaction file
    # else, return
    else:
        return
    return

def changeplan():
    # check session tupe, only accept if admin
    if session == "admin":
        # ask for name
        print("Please provide the account holder's name.")
        accountName = input()
        # check if exists
            # if not, prompt to try again

        # ask for account number
        print("Please provide an account number.")
        accNum = input()
        # check if exists
            # if not, prompt to try again
        # check if associated with name
            # if not, return to menu
        
        # change bank account plan to either student or non student (opposite whatever is currently selected)

        # save to bank account transaction file
    # else, return
    else:
        return
    
    return

def main():
    login()

if __name__ == "__main__":
    main()
