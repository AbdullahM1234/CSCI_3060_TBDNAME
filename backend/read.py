# read.py
# simple helper functions for backend input files

# reads old master accounts file into a dictionary
# format: NNNNN AAAAAAAAAAAAAAAAAAAA S PPPPPPPP TTTT
def read_old_bank_accounts(file_path):

    accounts = {}

    f = open(file_path, "r", encoding="utf-8")

    for raw in f:
        line = raw.rstrip("\n")

        if line == "":
            continue

        account_number = line[0:5]

        # remove underscore padding from name
        name = line[6:26].rstrip("_").strip()

        status = line[27]

        balance = float(line[29:38])

        total_transactions = int(line[39:43])

        accounts[account_number] = {
            "account_number": account_number,
            "name": name,
            "status": status,
            "balance": balance,
            "total_transactions": total_transactions,
            "plan": "NP",
            "session_count": 0
        }

    f.close()

    return accounts


def read_merged_transactions(file_path):

    transactions = []

    f = open(file_path, "r", encoding="utf-8")

    for raw in f:
        line = raw.strip()

        if line == "":
            continue

        parts = line.split()
        code = parts[0]

        tx = {
            "code": code,
            "raw": line,
            "account_number": "",
            "amount": 0.0,
            "name": "",
            "misc": ""
        }

        if code == "00":
            transactions.append(tx)

        elif code == "01":
            if len(parts) >= 3:
                tx["name"] = parts[2]
            transactions.append(tx)

        elif code == "02":
            if len(parts) >= 5:
                tx["account_number"] = parts[2]
                tx["amount"] = float(parts[3])
                tx["name"] = " ".join(parts[4:])
            transactions.append(tx)

        elif code == "03":
            if len(parts) >= 6:
                tx["account_number"] = parts[2]
                tx["misc"] = parts[3]
                tx["amount"] = float(parts[4])
                tx["name"] = " ".join(parts[5:])
            transactions.append(tx)

        elif code == "04":
            if len(parts) >= 6:
                tx["account_number"] = parts[2]
                tx["amount"] = float(parts[3])
                tx["misc"] = parts[4]
                tx["name"] = " ".join(parts[5:])
            transactions.append(tx)

        elif code == "05":
            if len(parts) >= 5:
                tx["account_number"] = parts[2]
                tx["amount"] = float(parts[3])
                tx["name"] = " ".join(parts[4:])
            transactions.append(tx)

        elif code == "06":
            if len(parts) >= 5:
                tx["account_number"] = parts[2]
                tx["name"] = parts[3]
                tx["amount"] = float(parts[4])
            transactions.append(tx)

        elif code == "07":
            if len(parts) >= 4:
                tx["account_number"] = parts[2]
                tx["name"] = " ".join(parts[3:])
            transactions.append(tx)

        elif code == "08":
            if len(parts) >= 4:
                tx["account_number"] = parts[2]
                tx["name"] = " ".join(parts[3:])
            transactions.append(tx)

        elif code == "09":
            if len(parts) >= 4:
                tx["account_number"] = parts[2]
                tx["name"] = " ".join(parts[3:])
            transactions.append(tx)

    f.close()

    return transactions