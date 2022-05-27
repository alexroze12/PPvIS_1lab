import argparse
import random
import shutil
from datetime import datetime
from Card import Card
from ATM import ATM
from Telephone import Telephone

file = open('config/ATM.txt', "r")
lines = file.readlines()
amount_of_storage_banknotes_in_my_ATM = eval(lines[0])
balance_on_your_card = int(lines[1])
status_of_card = lines[2]
cash_for_withdrawal = int(lines[3])

parser = argparse.ArgumentParser(description="This program is about ATM simulation")
parser.add_argument("p", type=int, help="Hello! Please, enter your pin:")
parser.add_argument("sp", type=int, help="Hello! Please, enter your pin:")
parser.add_argument("tp", type=int, help="Hello! Please, enter your pin:")
parser.add_argument("-b", "--balance", help="View balance", nargs="?", const=balance_on_your_card)
parser.add_argument("-w", "--withdrawal", type=int, help="Amount of withdrawal money", nargs="?")
parser.add_argument("-sw", "--sum_withdrawal", help="Summary amount of withdrawal money during the operation",
                    nargs="?", const=cash_for_withdrawal)
parser.add_argument("-u", "--unlock", help="Unlock card", nargs="?", const='locked')
parser.add_argument("-t", "--telephone_pay", type=int, help="Pay the telephone bill")
args = parser.parse_args()
money = ATM(amount_of_storage_banknotes_in_my_ATM)
belarusbank = Card(balance_on_your_card, cash_for_withdrawal)
bill = Telephone(random.randrange(0, 200, 1), belarusbank.card_balance)

if status_of_card == "locked\n":
    print("Sorry! Your card is blocked!")
    if args.unlock:
        status_of_card = status_of_card.replace("locked", "unlocked")
        with open("config/ATM.txt", "w") as file:
            file.write(str(money.amount_of_storage_banknotes))
        with open("config/ATM.txt", "a") as file:
            file.write("\n" + str(belarusbank.card_balance))
        with open("config/ATM.txt", "a") as file:
            file.write("\n" + str(status_of_card))
        with open("config/ATM.txt", "a") as file:
            file.write(str(belarusbank.cash_withdrawal))
    else:
        exit()
if args.p != int(belarusbank.password) and args.sp != int(belarusbank.password) and args.tp != int(belarusbank.password):
    print("Error! You have 0 attempts!")
    status_of_card = status_of_card.replace("unlocked", "locked")
    with open("config/ATM.txt", "w") as file:
        file.write(str(money.amount_of_storage_banknotes))
    with open("config/ATM.txt", "a") as file:
        file.write("\n" + str(belarusbank.card_balance))
    with open("config/ATM.txt", "a") as file:
        file.write("\n" + str(status_of_card))
    with open("config/ATM.txt", "a") as file:
        file.write(str(belarusbank.cash_withdrawal))
else:
    if args.balance:
        print(args.balance)
    if args.withdrawal:
        # a = args.balance - args.withdrawal
        # print(a)
        withdrawal_cash = belarusbank.withdrawal(args.withdrawal)
        shutil.copyfile("checks/Check.txt", "checks/Check_withdrawal.txt")
        with open("checks/Check_withdrawal.txt", "a") as document:
            current_date = datetime.now().date()
            document.write("DATE: " + str(current_date))
            current_time = datetime.now().time()
            document.write("\nTIME: " + str(current_time))
            document.write("\nCARD ACCOUNT: " + str(belarusbank.card_account))
            document.write("\nCASH WITHDRAWAL: " + str(withdrawal_cash))
            document.write("\n\nBANK APPROVED. CODE:000")
            document.write("\n\n      THANK YOU!")
    if args.sum_withdrawal:
        print(args.sum_withdrawal)
    if args.telephone_pay:
        card_balance = bill.pay_telephone(args.telephone_pay)
        shutil.copyfile("checks/Check_mobile.txt", "checks/Check_telephone_bill.txt")
        with open("checks/Check_telephone_bill.txt", "a") as material:
            current_date_mobile = datetime.now().date()
            material.write("DATE: " + str(current_date_mobile))
            current_time_mobile = datetime.now().time()
            material.write("\nTIME: " + str(current_time_mobile))
            material.write("\nCARD ACCOUNT: " + str(Card.card_account))
            material.write("\nMONEY TRANSFER TO PHONE: " + str(args.telephone_pay))
            material.write("\n\nBANK APPROVED. CODE:000")
            material.write("\n\n      THANK YOU!")
        file = open('config/ATM.txt', "r")
        lines_first = file.readlines()
        amount_of_banknotes = eval(lines_first[0])
        balance_of_your_card = lines_first[1]
        status_of_your_card = lines_first[2]
        cash_withdrawal = int(lines_first[3])
        counter_of_banknotes = ATM(amount_of_banknotes)
        final_cash_withdrawal = Card(balance_of_your_card, cash_withdrawal)
        with open("config/ATM.txt", "w") as files:
            files.write(str(counter_of_banknotes.amount_of_storage_banknotes))
        with open("config/ATM.txt", "a") as files:
            files.write("\n" + str(card_balance))
        with open("config/ATM.txt", "a") as files:
            files.write("\n" + status_of_your_card)
        with open("config/ATM.txt", "a") as files:
            files.write(str(final_cash_withdrawal.cash_withdrawal))
