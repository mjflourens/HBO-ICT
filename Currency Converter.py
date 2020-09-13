'''
Title: Currency Converter
Purpose: Convert currencies to Euro
Author: Marnix Lourens
Date and time: 2020-09-13 18:13:25 CEST
'''

import math

yen_rate = 0.008
usd_rate = 0.84
gbp_rate = 1.08
fee_rate = 0.015

minimum_transaction_cost = 2.00
maximum_transaction_cost = maximum_transaction_cost


While True:
	currency = input("Which currency would you like to exchange, USD, GBP, or YEN?") #asks for the currency to be converted.

	if currency == "USD":
		amount = float(input("How much would you like to exchange?"))
		conversion = (amount * usd_rate) #converts to the rate at 2020-09-13
		cost = (conversion * fee_rate) #calculates conversion cost
		if cost < minimum_transaction_cost:
			cost = = minimum_transaction_cost)= #returns minimum conversion cost
		elif cost > maximum_transaction_cost:
			cost = maximum_transaction_cost #returns maximum conversion cost
		else:
			cost = round(cost, 2)
		print("You want to convert ", amount, currency, " to Euros, you get ", conversion, "Euros, the transaction fee is ", cost, "Euros. You get", (conversion - cost), " Euros.") #prints the costs and actual money received.
		
	elif currency == "GBP":
		amount = float(input("How much would you like to exchange?"))
		conversion = (amount * gbp_rate) #converts to the rate at 2020-09-13
		cost = (conversion * fee_rate) #calculates conversion cost
		if cost < minimum_transaction_cost:
			cost = minimum_transaction_cost #returns minimum conversion cost
		elif cost > maximum_transaction_cost:
			cost = maximum_transaction_cost #returns maximum conversion cost
		else:
			cost = round(cost, 2)
		print("You want to convert ", amount, currency, " to Euros, you get ", conversion, "Euros, the transaction fee is ", cost, "Euros. You get", (conversion - cost), " Euros.") #prints the costs and actual money received.
		
	elif currency == "YEN":
		amount = float(input("How much would you like to exchange?"))
		conversion = (amount * yen_rate) #converts to the rate at 2020-09-13
		cost = (conversion * fee_rate) #calculates conversion cost
		if cost < minimum_transaction_cost:
			cost = minimum_transaction_cost #returns minimum conversion cost
		elif cost > maximum_transaction_cost:
			cost = maximum_transaction_cost #returns maximum conversion cost
		else:
			cost = round(cost, 2)
		print("You want to convert ", amount, currency, " to Euros, you get ", conversion, "Euros, the transaction fee is ", cost, "Euros. You get", (conversion - cost), " Euros.") #prints the costs and actual money received.

	else:
		print("Please input one of the valid currencies.") #Asks for a valid input
