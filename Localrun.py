
import random

Money = 800  # Starting money for pistol round

Side = input("Enter your side (CT or T): ").strip().upper() 
# CS2 pistol round buy options
ct_pistol_round_buys = {
    "P250" : 300,            # $300
    "Dual Berettas": 400,   # $400
    "Five-SeveN": 500,      # $500
    "CZ75-Auto": 500,       # $500
    "Kevlar Vest": 650,     # $650
    "Flashbang": 200,       # $200
    "Smoke Grenade": 300,   # $300
    "HE Grenade": 300,      # $300
    "Decoy Grenade": 50,   # $50
    "Defuse Kit": 400       # $400
}

t_pistol_round_buys = {
    "P250": 300,           # $300
    "Dual Berettas": 400,  # $400
    "Tec-9": 500,          # $500
    "CZ75-Auto": 500,      # $500
    "Kevlar Vest": 650,    # $650
    "Flashbang": 200,      # $200
    "Smoke Grenade": 300,  # $300
    "HE Grenade": 300,     # $300
    "Decoy Grenade": 50    # $50
}
if Side == "CT":
    buy_list = ct_pistol_round_buys
elif Side == "T":
    buy_list = t_pistol_round_buys
else:
    print("Invalid side entered. Please enter CT or T.")
    exit()

while True:
    output = random.choice(list(buy_list.items()))
    if output[1] <= Money:
        print(f"Random buy option for {Side}: {output[0]} (${output[1]})")
    Money -= output[1]
