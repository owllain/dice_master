import random

def roll_dice(num_dice, dice_size):
    total = 0
    for _ in range(num_dice):
        roll = random.randint(1, dice_size)
        total += roll
        print(f"Rolling a d{dice_size}... You rolled: {roll}")
    print(f"Total: {total}")

def main():
    print("Welcome to DiceMaster!")
    num_dice = int(input("Enter the number of dice to roll: "))
    dice_size = int(input("Enter the size of the dice (e.g., 6 for d6): "))
    roll_dice(num_dice, dice_size)

if __name__ == "__main__":
    main()

