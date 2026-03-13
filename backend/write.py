# write.py
# simple helper functions for backend output files

def write_new_master_accounts(accounts, file_path):
    # writes new master accounts file
    # format: NNNNN AAAAAAAAAAAAAAAAAAAA S PPPPPPPP TTTT

    f = open(file_path, "w", encoding="utf-8")

    for account_number in sorted(accounts.keys()):
        acc = accounts[account_number]

        acc_num = str(acc["account_number"]).zfill(5)
        name = acc["name"].ljust(20)[:20]
        status = acc["status"]
        balance = f"{acc['balance']:09.2f}"
        total_transactions = str(acc["total_transactions"]).zfill(4)

        line = f"{acc_num} {name} {status} {balance} {total_transactions}"
        f.write(line + "\n")

    f.close()


def write_new_current_accounts(accounts, file_path):
    # writes accounts.txt in the format frontend.py expects:
    # NAME ACCOUNT_NUMBER BALANCE STATUS PLAN

    f = open(file_path, "w", encoding="utf-8")

    for account_number in sorted(accounts.keys()):
        acc = accounts[account_number]

        name = acc["name"]
        acc_num = acc["account_number"]
        balance = f"{acc['balance']:.2f}"
        status = acc["status"]
        plan = acc["plan"]

        f.write(f"{name} {acc_num} {balance} {status} {plan}\n")

    f.write("END_OF_FILE 00000 0.00 D N\n")
    f.close()