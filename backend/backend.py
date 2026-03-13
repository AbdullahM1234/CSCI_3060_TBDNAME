# backend.py
# CSCI 3060U - Phase 4 Back End Preliminary Implementation


# Transaction codes used by the frontend transaction file
# 00 = End of session / end of file
# 01 = Login
# 02 = Withdraw
# 03 = Transfer
# 04 = Paybill
# 05 = Deposit
# 06 = Create
# 07 = Delete
# 08 = Disable
# 09 = Changeplan

# These records are written by frontend.py into the daily transaction file
# The backend reads the transaction file and processes each transaction sequentially.

from read import read_old_bank_accounts, read_merged_transactions
from write import write_new_master_accounts, write_new_current_accounts
import os

OLD_MASTER_FILE = "backend/MasterAccounts.txt"
TRANSACTION_FILE = "transactions/daily_transactions.atf"
NEW_MASTER_FILE = "backend/NewMasterAccounts.txt"
NEW_CURRENT_FILE = "accounts.txt"


def process_withdraw(accounts, transaction):
    account_number = transaction["account_number"]
    amount = transaction["amount"]

    accounts[account_number]["balance"] -= amount
    accounts[account_number]["total_transactions"] += 1


def process_deposit(accounts, transaction):
    account_number = transaction["account_number"]
    amount = transaction["amount"]

    accounts[account_number]["balance"] += amount
    accounts[account_number]["total_transactions"] += 1


def process_transfer(accounts, transaction):
    from_account = transaction["account_number"]
    to_account = transaction["misc"]
    amount = transaction["amount"]

    accounts[from_account]["balance"] -= amount
    accounts[to_account]["balance"] += amount
    accounts[from_account]["total_transactions"] += 1
    accounts[to_account]["total_transactions"] += 1


def process_paybill(accounts, transaction):
    account_number = transaction["account_number"]
    amount = transaction["amount"]

    accounts[account_number]["balance"] -= amount
    accounts[account_number]["total_transactions"] += 1


def process_create(accounts, transaction):
    account_number = transaction["account_number"]
    name = transaction["name"]

    accounts[account_number] = {
        "account_number": account_number,
        "name": name,
        "status": "A",
        "balance": 0.00,
        "total_transactions": 0,
        "plan": "NP",
    }


def process_delete(accounts, transaction):
    account_number = transaction["account_number"]

    del accounts[account_number]


def process_disable(accounts, transaction):
    account_number = transaction["account_number"]

    accounts[account_number]["status"] = "D"


def process_changeplan(accounts, transaction):
    account_number = transaction["account_number"]

    if accounts[account_number]["plan"] == "SP":
        accounts[account_number]["plan"] = "NP"
    else:
        accounts[account_number]["plan"] = "SP"


def process_transaction(accounts, transaction):
    code = transaction["code"]

    if code == "02":
        process_withdraw(accounts, transaction)

    elif code == "03":
        process_transfer(accounts, transaction)

    elif code == "04":
        process_paybill(accounts, transaction)

    elif code == "05":
        process_deposit(accounts, transaction)

    elif code == "06":
        process_create(accounts, transaction)

    elif code == "07":
        process_delete(accounts, transaction)

    elif code == "08":
        process_disable(accounts, transaction)

    elif code == "09":
        process_changeplan(accounts, transaction)

    elif code == "01":
        pass


def apply_service_fees(accounts):
    for account_number in accounts:
        if accounts[account_number]["plan"] == "NP":
            accounts[account_number]["balance"] -= 0.05


def main():
    accounts = read_old_bank_accounts(OLD_MASTER_FILE)
    transactions = read_merged_transactions(TRANSACTION_FILE)

    for transaction in transactions:
        if transaction["code"] == "00":
            continue

        process_transaction(accounts, transaction)

    apply_service_fees(accounts)

    write_new_master_accounts(accounts, NEW_MASTER_FILE)
    write_new_current_accounts(accounts, NEW_CURRENT_FILE)

    os.replace(NEW_MASTER_FILE, OLD_MASTER_FILE)


if __name__ == "__main__":
    main()