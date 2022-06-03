import unittest
from Controller.controller import Controller


class MyTestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(str(Controller.get_information_about_card_number()), "1234567812345678")

    def test_second(self):
        self.assertEqual(str(Controller.get_information_about_card_password()), "1234")

    def test_third(self):
        balance_on_your_card = Controller.get_information_about_card_balance()
        message = Controller.amount_of_withdrawal_money(str(1000))
        if message == "Correct":
            balance_on_your_card -= 1000
            Controller.set_information_about_card_balance(balance_on_your_card)
        self.assertEqual(balance_on_your_card, Controller.get_information_about_card_balance())

    def test_forth(self):
        balance_of_telephone = Controller.get_information_about_telephone_balance()
        Controller.pay_telephone_account(str(1000))
        self.assertEqual(balance_of_telephone + 1000, Controller.get_information_about_telephone_balance())

