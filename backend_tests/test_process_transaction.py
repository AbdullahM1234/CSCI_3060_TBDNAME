import sys
import os
import unittest

sys.path.append(os.path.abspath("backend"))

from backend import process_transaction


class TestProcessTransaction(unittest.TestCase):

    # process_transaction statement coverage -> Code02_test
    def test_code02_withdraw(self):
        accounts = {
            "12345": {
                "account_number": "12345",
                "name": "JOHN",
                "status": "A",
                "balance": 100.0,
                "total_transactions": 0,
                "plan": "NP"
            }
        }

        transaction = {
            "code": "02",
            "account_number": "12345",
            "amount": 40.0,
            "raw": "02 WITHDRAW 12345 40.0 JOHN"
        }

        process_transaction(accounts, transaction)

        self.assertEqual(accounts["12345"]["balance"], 60.0)
        self.assertEqual(accounts["12345"]["total_transactions"], 1)

    # process_transaction statement coverage -> Code03_test
    def test_code03_transfer(self):
        accounts = {
            "12345": {
                "account_number": "12345",
                "name": "JOHN",
                "status": "A",
                "balance": 100.0,
                "total_transactions": 0,
                "plan": "NP"
            },
            "22222": {
                "account_number": "22222",
                "name": "AMY",
                "status": "A",
                "balance": 200.0,
                "total_transactions": 0,
                "plan": "NP"
            }
        }

        transaction = {
            "code": "03",
            "account_number": "12345",
            "misc": "22222",
            "amount": 40.0,
            "raw": "03 TRANSFER 12345 22222 40.0 JOHN"
        }

        process_transaction(accounts, transaction)

        self.assertEqual(accounts["12345"]["balance"], 60.0)
        self.assertEqual(accounts["22222"]["balance"], 240.0)
        self.assertEqual(accounts["12345"]["total_transactions"], 1)
        self.assertEqual(accounts["22222"]["total_transactions"], 1)

    # process_transaction statement coverage -> Code04_test
    def test_code04_paybill(self):
        accounts = {
            "12345": {
                "account_number": "12345",
                "name": "JOHN",
                "status": "A",
                "balance": 100.0,
                "total_transactions": 0,
                "plan": "NP"
            }
        }

        transaction = {
            "code": "04",
            "account_number": "12345",
            "amount": 30.0,
            "raw": "04 PAYBILL 12345 30.0 COMPANY JOHN"
        }

        process_transaction(accounts, transaction)

        self.assertEqual(accounts["12345"]["balance"], 70.0)
        self.assertEqual(accounts["12345"]["total_transactions"], 1)

    # process_transaction statement coverage -> Code05_test
    def test_code05_deposit(self):
        accounts = {
            "12345": {
                "account_number": "12345",
                "name": "JOHN",
                "status": "A",
                "balance": 100.0,
                "total_transactions": 0,
                "plan": "NP"
            }
        }

        transaction = {
            "code": "05",
            "account_number": "12345",
            "amount": 50.0,
            "raw": "05 DEPOSIT 12345 50.0 JOHN"
        }

        process_transaction(accounts, transaction)

        self.assertEqual(accounts["12345"]["balance"], 150.0)
        self.assertEqual(accounts["12345"]["total_transactions"], 1)

    # process_transaction statement coverage -> Code06_test
    def test_code06_create(self):
        accounts = {}

        transaction = {
            "code": "06",
            "account_number": "99999",
            "name": "ALICE",
            "raw": "06 CREATE 99999 ALICE"
        }

        process_transaction(accounts, transaction)

        self.assertIn("99999", accounts)
        self.assertEqual(accounts["99999"]["account_number"], "99999")
        self.assertEqual(accounts["99999"]["name"], "ALICE")
        self.assertEqual(accounts["99999"]["status"], "A")
        self.assertEqual(accounts["99999"]["balance"], 0.0)
        self.assertEqual(accounts["99999"]["total_transactions"], 0)
        self.assertEqual(accounts["99999"]["plan"], "NP")

    # process_transaction statement coverage -> Code07_test
    def test_code07_delete(self):
        accounts = {
            "12345": {
                "account_number": "12345",
                "name": "JOHN",
                "status": "A",
                "balance": 100.0,
                "total_transactions": 0,
                "plan": "NP"
            }
        }

        transaction = {
            "code": "07",
            "account_number": "12345",
            "raw": "07 DELETE 12345 JOHN"
        }

        process_transaction(accounts, transaction)

        self.assertNotIn("12345", accounts)

    # process_transaction statement coverage -> Code08_test
    def test_code08_disable(self):
        accounts = {
            "12345": {
                "account_number": "12345",
                "name": "JOHN",
                "status": "A",
                "balance": 100.0,
                "total_transactions": 0,
                "plan": "NP"
            }
        }

        transaction = {
            "code": "08",
            "account_number": "12345",
            "raw": "08 DISABLE 12345 JOHN"
        }

        process_transaction(accounts, transaction)

        self.assertEqual(accounts["12345"]["status"], "D")

    # process_transaction statement coverage -> Code09_test
    def test_code09_changeplan(self):
        accounts = {
            "12345": {
                "account_number": "12345",
                "name": "JOHN",
                "status": "A",
                "balance": 100.0,
                "total_transactions": 0,
                "plan": "NP"
            }
        }

        transaction = {
            "code": "09",
            "account_number": "12345",
            "raw": "09 CHANGEPLAN 12345 JOHN"
        }

        process_transaction(accounts, transaction)

        self.assertEqual(accounts["12345"]["plan"], "SP")

    # process_transaction statement coverage -> Code01_test
    def test_code01_login(self):
        accounts = {
            "12345": {
                "account_number": "12345",
                "name": "JOHN",
                "status": "A",
                "balance": 100.0,
                "total_transactions": 0,
                "plan": "NP"
            }
        }

        transaction = {
            "code": "01",
            "raw": "01 LOGIN STANDARD 12345 JOHN"
        }

        process_transaction(accounts, transaction)

        self.assertEqual(accounts["12345"]["balance"], 100.0)
        self.assertEqual(accounts["12345"]["total_transactions"], 0)
        self.assertEqual(accounts["12345"]["plan"], "NP")
        self.assertEqual(accounts["12345"]["status"], "A")

    # process_transaction statement coverage -> CodeNa_test
    def test_codeNa_invalid_code(self):
        accounts = {
            "12345": {
                "account_number": "12345",
                "name": "JOHN",
                "status": "A",
                "balance": 100.0,
                "total_transactions": 0,
                "plan": "NP"
            }
        }

        transaction = {
            "code": "99",
            "account_number": "12345",
            "amount": 50.0,
            "raw": "99 UNKNOWN 12345 50.0 JOHN"
        }

        process_transaction(accounts, transaction)

        self.assertEqual(accounts["12345"]["balance"], 100.0)
        self.assertEqual(accounts["12345"]["total_transactions"], 0)
        self.assertEqual(accounts["12345"]["plan"], "NP")
        self.assertEqual(accounts["12345"]["status"], "A")


if __name__ == "__main__":
    unittest.main()