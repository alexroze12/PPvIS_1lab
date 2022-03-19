class ATM:
    storage_of_banknotes = {500: '500', 200: '200', 100: '100', 50: '50', 20: '20', 10: '10', 5: '5'}

    def __init__(self, amount_of_storage_banknotes):
        self.amount_of_storage_banknotes = amount_of_storage_banknotes
