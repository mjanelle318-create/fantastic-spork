import unittest
from bankaccount import BankAccount 

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Janelle", 100)

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 100)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    def test_withdraw(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.get_balance(), 70)

    def test_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(150)

    def test_multiple_transactions(self):
        self.account.deposit(50)
        self.account.deposit(25)
        self.account.withdraw(40)
        self.account.withdraw(10)
        self.assertEqual(self.account.get_balance(), 125)


if __name__ == "__main__":
    unittest.main()
