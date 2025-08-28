from bank_account_program import BankAccount
import unittest

class TestBankAccount(unittest.TestCase):

    # ssetUp() runs before each method to keep things constant
    def setUp(self):
        self.account = BankAccount("Alec", 100.0)

    ##### DEPOSIT TESTS #####

    def test_deposit_zero(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-50)

    def test_deposit_valid(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150.0)

    def test_deposit_float(self):
        self.account.deposit(50.73)
        self.assertEqual(self.account.get_balance(), 150.73)


    def test_deposit_large_amount(self):
        self.account.deposit(1000000000)
        self.assertEqual(self.account.get_balance(), 1000000100)

    def test_deposit_and_withdraw_sequence(self):
        self.account.deposit(100)
        self.account.withdraw(50)
        self.assertEqual(self.account.get_balance(), 150)

    def test_deposit_multiple_times(self):
        self.account.deposit(23)
        self.account.deposit(52)
        self.account.deposit(80)
        self.assertEqual(self.account.get_balance(), 255)

    ##### WITHDRAW TESTS #####

    def test_withdraw_valid(self):
        self.account.withdraw(40)
        self.assertEqual(self.account.get_balance(), 60.0)

    def test_withdraw_float(self):
        self.account.withdraw(49.50)
        self.assertEqual(self.account.get_balance(), 50.50)

    def test_withdraw_exact_balance(self):
        self.account.withdraw(100)
        self.assertEqual(self.account.get_balance(), 0.0)

    def test_withdraw_insufficient(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

    def test_withdraw_zero(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(0)

    def test_withdraw_negative(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-5)

    def test_withdraw_multiple_time(self):
        self.account.withdraw(5)
        self.account.withdraw(15)
        self.account.withdraw(25)
        self.account.withdraw(15)
        self.assertEqual(self.account.get_balance(), 40)

    def test_withdraw_until_empty(self):
        self.account.withdraw(5)
        self.account.withdraw(15)
        self.account.withdraw(25)
        self.account.withdraw(15)
        self.account.withdraw(3)
        self.account.withdraw(6)
        self.account.withdraw(1)
        self.account.withdraw(20)
        self.account.withdraw(10)
        self.assertEqual(self.account.get_balance(), 0)

    def test_large_withdraw_sequence(self):
        self.account.withdraw(50)
        self.account.withdraw(50)
        with self.assertRaises(ValueError):
            self.account.withdraw(50)

    ##### TRANSFER TESTS #####       

    def test_transfer_valid(self):
        other = BankAccount("Other", 50.0)
        self.account.transfer(other, 30)
        self.assertEqual(self.account.get_balance(), 70.0)
        self.assertEqual(other.get_balance(), 80.0)

    def test_transfer_insufficient(self):
        other = BankAccount("Other", 50.0)
        with self.assertRaises(ValueError):
            self.account.transfer(other, 200)

    def test_transfer_zero_amount(self):
        other = BankAccount("Other", 50.0)
        with self.assertRaises(ValueError):
            self.account.transfer(other, 0)

    def test_transfer_negative_amount(self):
        other = BankAccount("Other", 50.0)
        with self.assertRaises(ValueError):
            self.account.transfer(other, -50)

    def test_transfer_entire_balance(self):
        other = BankAccount("Other", 50.0)
        self.account.transfer(other, 100)
        self.assertEqual(self.account.get_balance(), 0.0)
        self.assertEqual(other.get_balance(), 150.0)

    def test_transfer_multiple_times(self):
        other = BankAccount("Other", 100.0)
        self.account.transfer(other, 50)
        other.transfer(self.account, 25)
        self.assertEqual(self.account.get_balance(), 75)
        self.assertEqual(other.get_balance(), 125)

    def test_transfer_to_empty_account(self):
        other = BankAccount("Other", 0.0)
        self.account.transfer(other, 50)
        self.assertEqual(self.account.get_balance(), 50)
        self.assertEqual(other.get_balance(), 50)

    def test_transfer_to_self(self):
        with self.assertRaises(ValueError):
            self.account.transfer(self.account, 10)

    def test_large_transfer_amount(self):
        other = BankAccount("Other", 100000000000000000.0)
        other.transfer(self.account, 5928278405)
        self.assertEqual(self.account.get_balance(), 5928278505)

    def test_transfers_between_three_accounts(self):
        other1 = BankAccount("Other1", 100.0)
        other2 = BankAccount("Other2", 100.0)
        self.account.transfer(other1, 50)
        other1.transfer(other2, 25)
        other2.transfer(self.account, 75)
        self.assertEqual(self.account.get_balance(), 125)
        self.assertEqual(other1.get_balance(), 125)
        self.assertEqual(other2.get_balance(), 50)

    ##### OTHER CASES #####

    def test_init_zero_balance(self):
        other = BankAccount("Other", 0.0)
        self.assertEqual(other.get_balance(), 0)

    def test_account_owner_name(self):
        other = BankAccount("Other", 0.0)
        self.assertEqual(other.owner, "Other")

    def test_balance_after_mixed_transactions(self):
        other = BankAccount("Other", 200.0)
        self.account.deposit(50)
        self.account.withdraw(25)
        self.account.transfer(other, 75)
        self.assertEqual(self.account.get_balance(), 50)
        self.assertEqual(other.get_balance(), 275)

    def test_account_str_format(self):
        self.assertEqual(str(self.account), "Account(Alec, Balance: 100.0)")


