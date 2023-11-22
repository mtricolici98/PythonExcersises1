money_5_coin = {
    "year_of_production": 2020,
    "type": "Coin",
    "drawing_on_back": "Stefan the great",
    "amount": 5,
}

money_10_paper = {
    "year_of_production": 2020,
    "type": "Paper",
    "drawing_on_back": "Stefan the great",
    "amount": 10,
}

card_from_maib = {
    "year_of_production": 2022,
    "type": "Card",
    "drawing_on_back": "Nistru River",
    "amount": "???",
}

wallet = [
    money_5_coin,
    money_5_coin,
    money_5_coin,
    money_10_paper,
    money_10_paper,
    card_from_maib
]

print(wallet[5]["type"])
#
# unit_from_wallet = wallet[4]
# print(unit_from_wallet)
# print(unit_from_wallet["type"])
