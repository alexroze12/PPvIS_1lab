class Telephone:

    def __init__(self, balance_of_telephone, card_balance):
        self.balance_of_telephone = balance_of_telephone
        self.card_balance = card_balance

    def pay_telephone(self, amount_of_money):
        file = open('config/ATM.txt', "r")
        lines_first = file.readlines()
        self.card_balance = int(lines_first[1])
        print(self.balance_of_telephone)
        self.balance_of_telephone = int(self.balance_of_telephone) + int(amount_of_money)
        self.card_balance = self.card_balance - int(amount_of_money)
        print("Successful: +" + str(amount_of_money))
        print("Telephone balance: " + str(self.balance_of_telephone))
        print("Card balance: " + str(self.card_balance))
        return self.card_balance
