
import random
import keyboard

Money = 8300  # Starting money (adjust as needed)

# Full buy options
buy_options = {
    # Pistols
    "Glock-18": 0, "USP-S": 0, "P2000": 0,
    "P250": 300, "Dual Berettas": 400, "Five-SeveN": 500, "Tec-9": 500, "CZ75-Auto": 500,
    "Desert Eagle": 700, "R8 Revolver": 600,

    # SMGs
    "MAC-10": 1050, "MP9": 1250, "MP7": 1500, "MP5-SD": 1500,
    "UMP-45": 1200, "P90": 2350, "PP-Bizon": 1400,

    # Rifles
    "Galil AR": 1800, "FAMAS": 2050, "AK-47": 2700, "M4A4": 3100, "M4A1-S": 2900,
    "SSG 08": 1700, "SG 553": 3000, "AUG": 3300, "AWP": 4750,
    "G3SG1": 5000, "SCAR-20": 5000,

    # Heavy
    "Nova": 1050, "XM1014": 2000, "MAG-7": 1300, "Sawed-Off": 1200,
    "M249": 5200, "Negev": 1700,

    # Grenades
    "Flashbang": 200, "Smoke Grenade": 300, "HE Grenade": 300,
    "Molotov": 400, "Incendiary": 600, "Decoy Grenade": 50,

    # Equipment
    "Kevlar Vest": 650, "Kevlar + Helmet": 1000, "Defuse Kit": 400, "Zeus x27": 200
}

while True:
    def random_buy():
        global Money
        affordable_items = [item for item, cost in buy_options.items() if cost <= Money]
        if not affordable_items:
            print("Not enough money to buy anything.")
            return
        item = random.choice(affordable_items)
        cost = buy_options[item]
        Money -= cost
        print(f"Bought: {item} for ${cost}. Remaining: ${Money}")

    # Bind 'b' to trigger random buy
    keyboard.add_hotkey('b', random_buy)

    print("Press 'B' to buy a random item. Press ESC to exit.")
    keyboard.wait('esc')
