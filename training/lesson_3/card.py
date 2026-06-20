class Card:
    number = '0000 0000 0000 0000'
    valdDate = '01/28'
    holder = 'unknown'

    def __init__(self, number, date, holder):
        self.holder = holder
        self.number = number
        self.valdDate = date

    def pay(self, amount):
        print('с карты', self.number, 'списали', amount)

