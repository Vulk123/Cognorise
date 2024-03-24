import random

def roll_dice(sides, rolls):
    results = [random.randint(1, sides) for _ in range(rolls)]
    return results

def main():
    print("Welcome to the Dice Rolling Simulator!")
    
    # Get user input for the number of sides and rolls
    sides = 6
    rolls = int(input("Enter the number of rolls: "))
    
    # Roll the dice and display the results
    results = roll_dice(sides, rolls)
    
    print(f"\nResults of rolling a {sides}-sided dice {rolls} times:")
    for i, result in enumerate(results, start=1):
        print(f"Roll {i}: {result}")

if __name__ == "__main__":
    main()
