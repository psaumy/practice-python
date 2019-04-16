class CoffeeCup(object):
    def __init__(self, name, innerCoffee=0):
        self.innerCoffee = innerCoffee
        self.owner = name

    def addCoffee(self, amount):
        self.innerCoffee += amount

    def releaseOneSip(self, sipSize):
        sip = sipSize
        if sipSize > self.innerCoffee:
            sip = self.innerCoffee
            self.innerCoffee = 0
        else:
            self.innerCoffee -= sipSize
        return sip

    def spillEntireContents(self):
        all = self.innerCoffee
        self.innerCoffee = 0
        return all

    def remaining_coffee(self):
        return self.owner + ': '+ str(self.innerCoffee) + ' ml'

    def drink_coffee(self, sipSize):
        sip = self.releaseOneSip(sipSize)
        return self.owner + ' drank ' + str(sip) + ' ml'


my_coffee_cup = CoffeeCup('Saumya')

rajat_s_coffee_cup = CoffeeCup('Rajat', 5)


my_coffee_cup.addCoffee(100)


print(my_coffee_cup.remaining_coffee())
print(rajat_s_coffee_cup.remaining_coffee())
print(my_coffee_cup.drink_coffee(30))
print(my_coffee_cup.spillEntireContents())
print(my_coffee_cup.remaining_coffee())
print(my_coffee_cup.drink_coffee(30))
print(my_coffee_cup.remaining_coffee())
print(my_coffee_cup.drink_coffee(30))
print(my_coffee_cup.remaining_coffee())
print(my_coffee_cup.drink_coffee(30))
print(my_coffee_cup.remaining_coffee())
print(my_coffee_cup.drink_coffee(30))
print(my_coffee_cup.remaining_coffee())
