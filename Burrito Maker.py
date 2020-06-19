
class Burrito:
     def tortilla(self):
        tortilla1 = input("Do you want Flour tortilla or Corn Tortilla:")
        print(tortilla1)
     def rice(self):
        rice1 = input("Do you want White Rice or Brown Rice:")
        print(rice1)
     def beans(self):
        beans1 = input("Do you want Black Beans or Pinto Beans:")
        print(beans1)
     def meat(self):
        meat1 = input("Do you want Chicken and Steak:")
        print(meat1)
     def salsa(self):
        salsa1 = input("Do you want Hot salsa or Mild salsa:")
        print(salsa1)
     def guacmole(self):
        beans1 = input("Do you want Guacmole or not:")
        print(beans1)
     def veggies(self):
        veggies1 = input("Do you want Veggies or not:")
        print(veggies1)
     def sour_cream(self):
        sour_cream1 = input("Do you want Sour Cream or not:")
        print(sour_cream1)
     def cheese(self):
        cheese1 = input("Do you want Cheese or not:")
        print(cheese1)
     def corn(self):
        sour_cream1 = input("Do you want Corn or not:")
        print(sour_cream1)
     def confirmation(self):
        print("Your order is confirmed. Your Yummy Burrito will be there in the next 5-10 min")


myBurrito = Burrito()

myBurrito.tortilla()
myBurrito.rice()
myBurrito.beans()
myBurrito.meat()
myBurrito.salsa()
myBurrito.guacmole()
myBurrito.veggies()
myBurrito.sour_cream()
myBurrito.cheese()
myBurrito.corn()
myBurrito.confirmation()

print("Your Bill is")
chicken_price = "8.00"
steak_price = "7.50"
cheese_price = "1.50"
guacmole_price = "2.00"
meat2 = print(input("Did you have Chicken or Steak"))
if meat2 == "Chicken" or "chicken":
    print("Your Burrito is $" + chicken_price)
else:
    print("Your Burrito is $" + steak_price)
cheese2 = print(input("Did you take cheese or not"))
if cheese2 == "Yes" or "yes" or "Y" or "y":
    print("There will be an additional charge of $" + cheese_price)
else:
    print("You wil have no additional charge")
guacmole2 = print(input("Did you take guacmole or not"))
if cheese2 == "Yes" or "yes" or "Y" or "y":
    print("There will be an additional charge of $" + guacmole_price)
else:
    print("You wil have no additional charge")

total_price = (float(chicken_price) + float(steak_price) + float(cheese_price) + float(guacmole_price))

print("Your Total Bill is $")
print(total_price)
