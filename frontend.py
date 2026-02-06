# global variables
username = "u"
password = "p"
session = "standard"

def login():

    # check if user has already logged in
    # i.e if username does not equal u

    # if user is logged in, error message and redirect to log out

    # else
    print("Welcome.")
    print("What session are you opening today? (admin or standard)\n")
    sessionType = input()

    if sessionType == "admin":
        print("admin selected.")
        session = "admin"

        # do not prompt for name input, move straight to menu

    else:
        print("standard selected.")
        username = input("Name: ") 
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

        print(f"Welcome, {username}.")

        # print account details

def logout():
    # check that user is logged in (username not default)
    
    # print transactions made during session

    # check for deposited money during session, add that to usable account funds

    # set account to available for transactions

    # reset name and session to default (not logged in)

    # log back in once logged out
    login()

def withdrawal():
    # check session and check login

    # check if available for transactions
        # if not, prompt to log out 

    # if admin, ask for account holder name

    # ask for account number
    # check account number is valid
        # if not, prompt to try again

    # ask for  withdrawal amount

    # check if more than $500
    # check that bank account will have at least $0 after transaction
        # if either true, reject withdrawal, return to menu

    # save to bank transaction file

    print()

def transfer():
    # check session and check login

    # check if available for transactions
        # if not, prompt to log out 

    # if admin, ask for account holder name

    # ask for account number 1
    # check if valid
        # if not, prompt to try again

    # ask for account number 2
    # check if valid
        # if not, prompt to try again 

    # ask for transfer ammount

    # check if more than $1000
    # check if back account 1 will have at least $0 after transfer
    # check that account 2 is not overdrafted
        # if any true, reject transfer, return to menu

    # save to bank transaction file
    print()

def paybill():
    # check session and check login

    # check if available for transactions
        # if not, prompt to log out 

    # if admin, ask for account holder name

    # ask for account number
    # check if valid
        # if not, prompt to try again

    # ask for payee
    # check if valid payee
        # if not, prompt to try again

    # ask for bill pay amount

    # check if more than $2000
    # check if account will have at least $0 after payment
        # if either, reject payment and return to menu

    # save to bank transaction file

    print()

def deposit():
    # check session and check login

    # check if available for transactions
        # if not, prompt to log out 

    # if admin, ask for account holder name

    # ask for account number
    # check if valid
        # if not, prompt to try again
    
    # ask for deposit amount

    # save to bank transaction file

    # store to be added at end of session
    print()

def create():
    # check session type, only accept if admin

    # else, return

    # ask for name
    # check if exists
        # if it does, prompt to try again
    # check if name is more than 20 characters
        # if it is, prompt to try again

    # ask for inital account balance
    # check if less than $99999.99
        # if not, prompt to try again

    # generate random account number

    # save and print info to bank transaction file

    # note to not allow transactions on this account until session ends
    print()

def delete():
    # check session type, only accept if admin

    # else, return

    # ask for name
    # check if exists
        # if not, prompt to try again
    
    # ask for account number
    # check if exists
        # if not, prompt to try again
    # check if associated with name
        # if not, return to menu
    
    # save to bank transaction file

    # set data to deleted

    print()

def disable():
    # check session type, only accept if admin

    # else, return

    # ask for name
    # check if exists
        # if not, prompt to try again

    # ask for account number
    # check if exists
        # if not, prompt to try again
    # check if associated with name
        # if not, return to menu
    
    # change bank account status to disabled and no transactions
    # save to bank account transaction file
    print()

def changeplan():
    # check session tupe, only accept if admin

    # else, return

    # ask for name
    # check if exists
        # if not, prompt to try again
    
    # ask for account number
    # check if exists
        # if not, prompt to try again
    # check if associated with name
        # if not, return to menu
    
    # change bank account plan to either student or non student (opposite whatever is currently selected)

    # save to bank account transaction file
    print()

def main():
    login()

if __name__ == "__main__":
    main()