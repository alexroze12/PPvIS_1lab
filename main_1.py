import random
import shutil
from datetime import datetime
from Bank import Bank
from Card import Card
from ATM import ATM
from Telephone import Telephone


file = open('ATM.txt', "r")
lines = file.readlines()
amount_of_storage_banknotes_in_my_ATM = eval(lines[0])
balance_on_your_card = int(lines[1])
status_of_card = lines[2]
cash_for_withdrawal = int(lines[3])
money = ATM(amount_of_storage_banknotes_in_my_ATM)
belarusbank = Card(balance_on_your_card, cash_for_withdrawal)
bill = Telephone(random.randrange(0, 200, 1), belarusbank.card_balance)
bank_telephone = Bank()

if status_of_card == "locked\n":
    print("Sorry! Your card is blocked!")
    print("Would you like to use bank phone to unlock your card? 1- Yes' or 2- 'No': ")
    y = int(input())
    if y == 1:
        status_of_card = status_of_card.replace("locked", "unlocked")
        with open("ATM.txt", "w") as file:
            file.write(str(money.amount_of_storage_banknotes))
        with open("ATM.txt", "a") as file:
            file.write("\n" + str(belarusbank.card_balance))
        with open("ATM.txt", "a") as file:
            file.write("\n" + str(status_of_card))
        with open("ATM.txt", "a") as file:
            file.write(str(belarusbank.cash_withdrawal))
    elif y == 2:
        print("Sorry! Your card is blocked!")
        exit()
for i in range(2, -1, -1):
    print("Hello! Please, enter your pin: ")
    pin = input()
    if len(pin) != 4 or pin != belarusbank.password:
        print("Error! You have "+str(i) + " attempts!")
        if i == 0:
            print("Your card is blocked! Please contact your bank to resolve the issue!")
            status_of_card = status_of_card.replace("unlocked", "locked")
            with open("ATM.txt", "w") as file:
                file.write(str(money.amount_of_storage_banknotes))
            with open("ATM.txt", "a") as file:
                file.write("\n" + str(belarusbank.card_balance))
            with open("ATM.txt", "a") as file:
                file.write("\n" + str(status_of_card))
            with open("ATM.txt", "a") as file:
                file.write(str(belarusbank.cash_withdrawal))
            print("You can use this telephone number: " + str(bank_telephone.telephone))
            print("Would you like to use this phone to unlock your card? 1- Yes' or 2- 'No': ")
            try:
                y = int(input())
            except ValueError:
                print("Failed")
                raise
            if y == 1:
                print("Congratulations! Your card is unlocked!")
                file = open('ATM.txt', "r")
                line = file.readlines()
                status = line[2]
                status = status.replace("locked", "unlocked")
                with open("ATM.txt", "w") as file:
                    file.write(str(money.amount_of_storage_banknotes))
                with open("ATM.txt", "a") as file:
                    file.write("\n" + str(belarusbank.card_balance))
                with open("ATM.txt", "a") as file:
                    file.write("\n" + str(status))
                with open("ATM.txt", "a") as file:
                    file.write(str(belarusbank.cash_withdrawal))
            elif y == 2:
                print("Sorry! Your card is blocked!")
                exit()
    else:
        break
print("Please, choose an operation: ")
while True:
    file = open('ATM.txt', "r")
    lines = file.readlines()
    balance_on_your_card = int(lines[1])
    amount_of_banknotes = eval(lines[0])
    cash_for_withdrawal_on_your_card = int(lines[3])
    belarusbank = Card(balance_on_your_card, cash_for_withdrawal)
    counter_of_banknotes_in_ATM = ATM(amount_of_banknotes)
    print("""1. Check the balance
2. Withdrawal
3. Pay the telephone bill
4. Finish our operations""")

    print("Your choice: ")
    try:
        x = int(input())
    except ValueError:
        print("Failed")
        raise
    if x == 1:
        print(belarusbank.card_balance)

    elif x == 2:
        print("Necessary amount of money: ")
        key = int(input())
        if key % 10 != 0:
            print("Enter the correct amount!")
            continue
        if key > belarusbank.card_balance:
            print("Requested amount is greater than current balance. Enter the correct amount!")
            continue
        belarusbank.withdrawal(key)
    elif x == 3:
        print("Please, enter the telephone number (9 numbers): ")
        number = input("+375")
        if len(number) != 9:
            print("Enter the correct amount!")
            continue
        print("Necessary amount of money: ")
        money = input()
        bill.pay_telephone(money)
    elif x == 4:
        print("Thank you! Would you like to get a check?")
        print("Please, choose 1- Yes' or 2- 'No': ")
        try:
            y = int(input())
        except ValueError:
            print("Failed")
            raise
        if y == 1:
            shutil.copyfile("D:\\Python\\Check.txt", "D:\\Python\\Check_withdrawal.txt")
            with open("Check_withdrawal.txt", "a") as document:
                current_date = datetime.now().date()
                document.write("DATE: " + str(current_date))
                current_time = datetime.now().time()
                document.write("\nTIME: " + str(current_time))
                document.write("\nCARD ACCOUNT: " + str(belarusbank.card_account))
                document.write("\nCASH WITHDRAWAL: " + str(cash_for_withdrawal_on_your_card))
                document.write("\n\nBANK APPROVED. CODE:000")
                document.write("\n\n      THANK YOU!")

        elif y == 2:
            print("Goodbye!")
            remainder_cash_for_withdrawal_to_delete = "0"
            with open("ATM.txt", "w") as files:
                files.write(str(counter_of_banknotes_in_ATM.amount_of_storage_banknotes))
            with open("ATM.txt", "a") as files:
                files.write("\n" + str(belarusbank.card_balance))
            with open("ATM.txt", "a") as files:
                files.write("\n" + str(status_of_card))
            with open("ATM.txt", "a") as files:
                files.write(str(remainder_cash_for_withdrawal_to_delete))
            break
