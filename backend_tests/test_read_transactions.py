import sys
import os
import unittest

sys.path.append(os.path.abspath("backend"))

from read import read_merged_transactions


class TestReadMergedTransactions(unittest.TestCase):

    # read_merged_transactions decision and loop coverage -> file_DNE_test
    def test_file_DNE(self):
        with self.assertRaises(FileNotFoundError):
            read_merged_transactions("backend_tests/does_not_exist.atf")

    # read_merged_transactions decision and loop coverage -> Code00_test
    def test_code00(self):
        file_path = "backend_tests/test_code00.atf"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write("00\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "00")

        os.remove(file_path)

    # read_merged_transactions decision and loop coverage -> Code01_test
    def test_code01(self):
        file_path = "backend_tests/test_code01.atf"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write("01 LOGIN STANDARD 12345 JOHN\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "01")

        os.remove(file_path)

    # read_merged_transactions decision and loop coverage -> Code02_test
    def test_code02(self):
        file_path = "backend_tests/test_code02.atf"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write("02 WITHDRAW 12345 50.00 JOHN\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "02")
        self.assertEqual(transactions[0]["account_number"], "12345")
        self.assertEqual(transactions[0]["amount"], 50.00)

        os.remove(file_path)

            # read_merged_transactions decision and loop coverage -> Code03_test
    def test_code03(self):
        file_path = "backend_tests/test_code03.atf"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write("03 TRANSFER 12345 22222 40.00 JOHN\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "03")
        self.assertEqual(transactions[0]["account_number"], "12345")
        self.assertEqual(transactions[0]["misc"], "22222")
        self.assertEqual(transactions[0]["amount"], 40.00)

        os.remove(file_path)

    # read_merged_transactions decision and loop coverage -> Code04_test
    def test_code04(self):
        file_path = "backend_tests/test_code04.atf"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write("04 PAYBILL 12345 25.00 COMPANY JOHN\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "04")
        self.assertEqual(transactions[0]["account_number"], "12345")
        self.assertEqual(transactions[0]["amount"], 25.00)

        os.remove(file_path)

    # read_merged_transactions decision and loop coverage -> Code05_test
    def test_code05(self):
        file_path = "backend_tests/test_code05.atf"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write("05 DEPOSIT 12345 75.00 JOHN\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "05")
        self.assertEqual(transactions[0]["account_number"], "12345")
        self.assertEqual(transactions[0]["amount"], 75.00)

        os.remove(file_path)

    # read_merged_transactions decision and loop coverage -> Code06_test
    def test_code06(self):
        file_path = "backend_tests/test_code06.atf"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write("06 CREATE 99999 ALICE\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "06")
        self.assertEqual(transactions[0]["account_number"], "99999")
        self.assertEqual(transactions[0]["name"], "ALICE")

        os.remove(file_path)

    # read_merged_transactions decision and loop coverage -> Code07_test
    def test_code07(self):
        file_path = "backend_tests/test_code07.atf"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write("07 DELETE 12345 JOHN\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "07")
        self.assertEqual(transactions[0]["account_number"], "12345")

        os.remove(file_path)

    # read_merged_transactions decision and loop coverage -> Code08_test
    def test_code08(self):
        file_path = "backend_tests/test_code08.atf"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write("08 DISABLE 12345 JOHN\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "08")
        self.assertEqual(transactions[0]["account_number"], "12345")

        os.remove(file_path)

    # read_merged_transactions decision and loop coverage -> Code09_test
    def test_code09(self):
        file_path = "backend_tests/test_code09.atf"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write("09 CHANGEPLAN 12345 JOHN\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "09")
        self.assertEqual(transactions[0]["account_number"], "12345")

        os.remove(file_path)

# if false tests

    # read_merged_transactions decision and loop coverage -> Code02_false_test
    def test_code02_false(self):
        file_path = "backend_tests/test_code02_false.atf"

        # Missing amount and name → len(parts) too small
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("02 WITHDRAW 12345\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "02")
        # account_number may still exist, but amount should be default (0.0)
        self.assertEqual(transactions[0]["account_number"], "")
        self.assertEqual(transactions[0]["amount"], 0.0)

        os.remove(file_path)

    # read_merged_transactions decision and loop coverage -> Code03_false_test
    def test_code03_false(self):
        file_path = "backend_tests/test_code03_false.atf"

        # Missing destination account and amount → len(parts) too small
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("03 TRANSFER 12345\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "03")
        # fields should remain default due to insufficient parts
        self.assertEqual(transactions[0]["account_number"], "")
        self.assertEqual(transactions[0]["misc"], "")
        self.assertEqual(transactions[0]["amount"], 0.0)

        os.remove(file_path)

    # read_merged_transactions decision and loop coverage -> Code04_false_test
    def test_code04_false(self):
        file_path = "backend_tests/test_code04_false.atf"

        # Missing amount → len(parts) too small
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("04 PAYBILL 12345\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "04")
        # fields remain default due to insufficient parts
        self.assertEqual(transactions[0]["account_number"], "")
        self.assertEqual(transactions[0]["amount"], 0.0)

        os.remove(file_path)

    # read_merged_transactions decision and loop coverage -> Code05_false_test
    def test_code05_false(self):
        file_path = "backend_tests/test_code05_false.atf"

        # Missing amount → len(parts) too small
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("05 DEPOSIT 12345\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "05")
        # fields remain default due to insufficient parts
        self.assertEqual(transactions[0]["account_number"], "")
        self.assertEqual(transactions[0]["amount"], 0.0)

        os.remove(file_path)

    # read_merged_transactions decision and loop coverage -> Code06_false_test
    def test_code06_false(self):
        file_path = "backend_tests/test_code06_false.atf"

        # Missing name → len(parts) too small
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("06 CREATE 99999\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "06")
        # fields remain default due to insufficient parts
        self.assertEqual(transactions[0]["account_number"], "")
        self.assertEqual(transactions[0]["name"], "")

        os.remove(file_path)

    # read_merged_transactions decision and loop coverage -> Code07_false_test
    def test_code07_false(self):
        file_path = "backend_tests/test_code07_false.atf"

        # Missing account number → len(parts) too small
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("07 DELETE\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "07")
        # fields remain default due to insufficient parts
        self.assertEqual(transactions[0]["account_number"], "")

        os.remove(file_path)

    # read_merged_transactions decision and loop coverage -> Code08_false_test
    def test_code08_false(self):
        file_path = "backend_tests/test_code08_false.atf"

        # Missing account number → len(parts) too small
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("08 DISABLE\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "08")
        # fields remain default due to insufficient parts
        self.assertEqual(transactions[0]["account_number"], "")

        os.remove(file_path)

    # read_merged_transactions decision and loop coverage -> Code09_false_test
    def test_code09_false(self):
        file_path = "backend_tests/test_code09_false.atf"

        # Missing account number → len(parts) too small
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("09 CHANGEPLAN\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "09")
        # fields remain default due to insufficient parts
        self.assertEqual(transactions[0]["account_number"], "")

        os.remove(file_path)

# if true tests

    # read_merged_transactions decision and loop coverage -> file_02Transaction_if_test
    def test_code02_if(self):
        file_path = "backend_tests/test_code02_if.atf"

        # len(parts) >= 5 → TRUE branch
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("02 WITHDRAW 12345 50.00 JOHN\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "02")
        self.assertEqual(transactions[0]["account_number"], "12345")
        self.assertEqual(transactions[0]["amount"], 50.00)

        os.remove(file_path)

    # read_merged_transactions decision and loop coverage -> file_03Transaction_if_test
    def test_code03_if(self):
        file_path = "backend_tests/test_code03_if.atf"

        # len(parts) >= 6 -> TRUE branch
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("03 TRANSFER 12345 22222 40.00 JOHN\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "03")
        self.assertEqual(transactions[0]["account_number"], "12345")
        self.assertEqual(transactions[0]["misc"], "22222")
        self.assertEqual(transactions[0]["amount"], 40.00)

        os.remove(file_path)

    # read_merged_transactions decision and loop coverage -> file_04Transaction_if_test
    def test_code04_if(self):
        file_path = "backend_tests/test_code04_if.atf"

        # len(parts) >= 6 -> TRUE branch
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("04 PAYBILL 12345 COMPANY 25.00 JOHN\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "04")
        self.assertEqual(transactions[0]["account_number"], "12345")
        self.assertEqual(transactions[0]["amount"], 25.00)

        os.remove(file_path)

    # read_merged_transactions decision and loop coverage -> file_05Transaction_if_test
    def test_code05_if(self):
        file_path = "backend_tests/test_code05_if.atf"

        # len(parts) >= 5 -> TRUE branch
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("05 DEPOSIT 12345 75.00 JOHN\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "05")
        self.assertEqual(transactions[0]["account_number"], "12345")
        self.assertEqual(transactions[0]["amount"], 75.00)

        os.remove(file_path)

    # read_merged_transactions decision and loop coverage -> file_06Transaction_if_test
    def test_code06_if(self):
        file_path = "backend_tests/test_code06_if.atf"

        # len(parts) >= 5 -> TRUE branch
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("06 CREATE 99999 ALICE\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "06")
        self.assertEqual(transactions[0]["account_number"], "99999")
        self.assertEqual(transactions[0]["name"], "ALICE")

        os.remove(file_path)

    # read_merged_transactions decision and loop coverage -> file_07Transaction_if_test
    def test_code07_if(self):
        file_path = "backend_tests/test_code07_if.atf"

        # len(parts) >= 4 -> TRUE branch
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("07 DELETE 12345 JOHN\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "07")
        self.assertEqual(transactions[0]["account_number"], "12345")

        os.remove(file_path)
        
    # read_merged_transactions decision and loop coverage -> file_08Transaction_if_test
    def test_code08_if(self):
        file_path = "backend_tests/test_code08_if.atf"

        # len(parts) >= 4 -> TRUE branch
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("08 DISABLE 12345 JOHN\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "08")
        self.assertEqual(transactions[0]["account_number"], "12345")

        os.remove(file_path)

    # read_merged_transactions decision and loop coverage -> file_09Transaction_if_test
    def test_code09_if(self):
        file_path = "backend_tests/test_code09_if.atf"

        # len(parts) >= 4 -> TRUE branch
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("09 CHANGEPLAN 12345 JOHN\n")

        transactions = read_merged_transactions(file_path)

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["code"], "09")
        self.assertEqual(transactions[0]["account_number"], "12345")

        os.remove(file_path)

if __name__ == "__main__":
    unittest.main()