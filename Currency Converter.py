'''
Title: Currency Converter
Purpose: Convert currencies to Euro
Author: Marnix Lourens
Date and time: 2020-09-13 18:13:25 CEST
'''

import math
#this is a comment
currency = input("Which currency would you like to exchange, USD, GBP, or YEN?") #asks for the currency to be converted.

if currency == "USD":
	amount = float(input("How much would you like to exchange?"))
	conversion = (amount * 0.84) #converts to the rate at 2020-09-13
	cost = (conversion * 0.015) #calculates conversion cost
	if cost < 2:
		cost = float(2.00) #returns minimum conversion cost
	elif cost > 15:
		cost = float(15.00) #returns maximum conversion cost
	else:
		cost = round(cost, 2)
	print("You want to convert ", amount, currency, " to Euros, you get ", conversion, "Euros, the transaction fee is ", cost, "Euros. You get", (conversion - cost), " Euros.") #prints the costs and actual money received.
	
elif currency == "GBP":
	amount = float(input("How much would you like to exchange?"))
	conversion = (amount * 1.08) #converts to the rate at 2020-09-13
	cost = (conversion * 0.015) #calculates conversion cost
	if cost < 2:
		cost = float(2.00) #returns minimum conversion cost
	elif cost > 15:
		cost = float(15.00) #returns maximum conversion cost
	else:
		cost = round(cost, 2)
	print("You want to convert ", amount, currency, " to Euros, you get ", conversion, "Euros, the transaction fee is ", cost, "Euros. You get", (conversion - cost), " Euros.") #prints the costs and actual money received.
	
elif currency == "YEN":
	amount = float(input("How much would you like to exchange?"))
	conversion = (amount * 0.008) #converts to the rate at 2020-09-13
	cost = (conversion * 0.015) #calculates conversion cost
	if cost < 2:
		cost = float(2.00) #returns minimum conversion cost
	elif cost > 15:
		cost = float(15.00) #returns maximum conversion cost
	else:
		cost = round(cost, 2)
	print("You want to convert ", amount, currency, " to Euros, you get ", conversion, "Euros, the transaction fee is ", cost, "Euros. You get", (conversion - cost), " Euros.") #prints the costs and actual money received.

else:
	print("Please input one of the valid currencies.") #Asks for a valid input
