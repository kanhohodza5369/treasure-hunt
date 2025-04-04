# Treasure Hunt Game

print("Welcome to the Treasure Hunt Game!")
print("You are standing in a forest. The treasure is hidden somewhere.")
print("You can go north, south, east, or west.")

# Game Data
treasure_location = "east"

# Game Loop
while True:
    direction = input("Which direction do you want to go? (north/south/east/west): ").lower()
    
    if direction == treasure_location:
        print("Congratulations! You found the treasure!")
        break
    elif direction == "north":
        print("You went north. You are now in a river. The treasure is not here.")
    elif direction == "south":
        print("You went south. You are now in a mountain. The treasure is not here.")
    elif direction == "west":
        print("You went west. You are now in a desert. The treasure is not here.")
    else:
        print("Invalid direction. Please try again.")

