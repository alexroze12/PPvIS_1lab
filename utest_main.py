import unittest
import ATM
import Card
import Telephone


class MyTestCase(unittest.TestCase):
    def first_test(self):
        self.assertEqual(str(Card.Card.card_account), "1234543267890123")

    def second_test(self):
        self.assertEqual(str(Card.Card.password), "1234")

    def third_test(self):
        file = open('ATM.txt', "r")
        lines = file.readlines()
        amount_of_storage_banknotes = eval(lines[0])
        balance_on_your_card = int(lines[1])
        cash_for_withdrawal = int(lines[3])
        file.close()
        m = Card.Card(balance_on_your_card, cash_for_withdrawal)
        s = ATM.ATM(amount_of_storage_banknotes)
        Card.Card.withdrawal(m, 1000)
        with open("Tests.txt", "w") as file:
            file.write(str(s.amount_of_storage_banknotes))
        with open("Tests.txt", "a") as file:
            file.write("\n" + str(m.card_balance))
        file.close()
        file = open('Tests.txt', "r")
        lines = file.readlines()
        balance_on_your_card = int(lines[1])
        self.assertEqual(balance_on_your_card, 12500)

    def forth_test(self):
        file = open('ATM.txt', "r")
        lines = file.readlines()
        balance_on_your_card = int(lines[1])
        m = Telephone.Telephone(1000, balance_on_your_card)
        m.pay_telephone(1000)
        self.assertEqual(m.balance_of_telephone, 2000)
if __name__ == '__main__':
    unittest.main()
