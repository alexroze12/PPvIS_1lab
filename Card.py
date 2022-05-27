from ATM import ATM


class Card:
    password: str = "1234"
    card_account: str = "1234543267890123"

    def __init__(self, card_balance, cash_withdrawal):
        self.card_balance = card_balance
        self.cash_withdrawal = cash_withdrawal

    def withdrawal(self, nominal):
        global amount_of_banknotes, banknote
        files = open('config/ATM.txt', "r")
        line_second = files.readlines()
        ATM.amount_of_storage_banknotes = eval(line_second[0])
        self.cash_withdrawal = int(line_second[3])
        status_of_card = line_second[2]
        self.cash_withdrawal = nominal + self.cash_withdrawal
        while nominal != 0:
            print("Please, choose necessary banknotes: 500 200 100 50 20 10 5 ")
            banknote = int(input())
            print("The number of banknotes of this type in the ATM: " + str(
                ATM.amount_of_storage_banknotes[str(banknote)]))
            print("Choose amount: ")
            try:
                amount_of_banknotes = int(input())
            except ValueError:
                print("Failed")
                raise
            if ATM.amount_of_storage_banknotes.get(str(banknote)) - amount_of_banknotes >= 0 and nominal - (
                    amount_of_banknotes * banknote) > 0:
                ATM.amount_of_storage_banknotes.update(
                    {str(banknote): (ATM.amount_of_storage_banknotes.get(str(banknote)) - amount_of_banknotes)})

            elif ATM.amount_of_storage_banknotes.get(str(banknote)) - amount_of_banknotes < 0:
                print(
                    "Choose other banknotes or another amount! The number of banknotes of this type in the ATM: " + str(
                        ATM.amount_of_storage_banknotes[str(banknote)]))
                continue
            self.card_balance = self.card_balance - (amount_of_banknotes*banknote)
            if nominal - (amount_of_banknotes*banknote) < 0:
                print("You have entered an amount that is more than requested! Please, enter correct data!")
            else:
                nominal = nominal - (amount_of_banknotes*banknote)
            print("The remaining amount to be withdrawn: "+str(nominal))
        ATM.amount_of_storage_banknotes.update(
            {str(banknote): (ATM.amount_of_storage_banknotes.get(str(banknote)) - amount_of_banknotes)})
        print("Card balance: "+str(self.card_balance))
        with open("config/ATM.txt", "w") as my_file:
            my_file.write(str(ATM.amount_of_storage_banknotes))
        with open("config/ATM.txt", "a") as my_file:
            my_file.write("\n"+str(self.card_balance))
        with open("config/ATM.txt", "a") as my_file:
            my_file.write("\n" + status_of_card)
        with open("config/ATM.txt", "a") as my_file:
            my_file.write(str(self.cash_withdrawal))
        return self.cash_withdrawal
