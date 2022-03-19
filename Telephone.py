from Card import Card
from ATM import ATM
import shutil
from datetime import datetime


class Telephone:

    def __init__(self, balance_of_telephone, card_balance):
        self.balance_of_telephone = balance_of_telephone
        self.card_balance = card_balance

    def pay_telephone(self, amount_of_money):
        file = open('ATM.txt', "r")
        lines_first = file.readlines()
        self.card_balance = int(lines_first[1])
        print(self.balance_of_telephone)
        self.balance_of_telephone = int(self.balance_of_telephone) + int(amount_of_money)
        self.card_balance = self.card_balance - int(amount_of_money)
        print("Successful: +" + str(amount_of_money))
        print("Telephone balance: " + str(self.balance_of_telephone))
        print("Card balance: " + str(self.card_balance))
        print("Thank you! Would you like to get a check?")
        print("Please, choose 1- Yes' or 2- 'No': ")
        try:
            m = int(input())
        except ValueError:
            print("Failed")
            raise
        if m == 1:
            shutil.copyfile("D:\\Python\\Check_mobile.txt", "D:\\Python\\Check_telephone_bill.txt")
            with open("Check_telephone_bill.txt", "a") as material:
                current_date_mobile = datetime.now().date()
                material.write("DATE: " + str(current_date_mobile))
                current_time_mobile = datetime.now().time()
                material.write("\nTIME: " + str(current_time_mobile))
                material.write("\nCARD ACCOUNT: " + str(Card.card_account))
                material.write("\nMONEY TRANSFER TO PHONE: " + str(amount_of_money))
                material.write("\n\nBANK APPROVED. CODE:000")
                material.write("\n\n      THANK YOU!")
        elif m == 2:
            print("Thank you! Would you like to do anything?")
        amount_of_banknotes = eval(lines_first[0])
        balance_of_your_card = lines_first[1]
        status_of_your_card = lines_first[2]
        cash_withdrawal = int(lines_first[3])
        counter_of_banknotes = ATM(amount_of_banknotes)
        final_cash_withdrawal = Card(balance_of_your_card, cash_withdrawal)
        with open("ATM.txt", "w") as files:
            files.write(str(counter_of_banknotes.amount_of_storage_banknotes))
        with open("ATM.txt", "a") as files:
            files.write("\n" + str(self.card_balance))
        with open("ATM.txt", "a") as files:
            files.write("\n" + status_of_your_card)
        with open("ATM.txt", "a") as files:
            files.write(str(final_cash_withdrawal.cash_withdrawal))
