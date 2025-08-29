
import random
import keyboard


# Full buy options: list of key sequences
buy_options = [
    ("1", "1"),
    ("1", "2"),
    ("1", "3"),
    ("1", "4"),
    ("2", "1"),
    ("2", "2"),
    ("2", "3"),
    ("2", "4"),
    ("3", "1"),
    ("3", "2"),
    ("3", "3"),
    ("3", "4"),
    ("3", "5"),
    ("4", "1"),
    ("4", "2"),
    ("4", "3"),
    ("4", "4"),
    ("4", "5"),
    ("5", "1"),
    ("5", "2"),
    ("5", "3"),
    ("5", "4"),
    ("5", "5"),
]


def random_buy():
    for i in range(3):
        keys = random.choice(buy_options)
        print(f"Inputting {i+1}: {keys}")
        for key in keys:
            keyboard.send(key)

# Bind 'b' to trigger random buy
keyboard.add_hotkey('b', random_buy)

print("Press 'B' to buy a random item. Press ESC to exit.")
keyboard.wait('esc')