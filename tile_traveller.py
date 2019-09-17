# Unnið af Vésteini Bjarnasyni og Yngvi Leó Þráinsson
# Create a game a game that consist of a 3x3 grid
# Where the player can only move in a fixed direction
# based on the tile he's at
# The player starts at tile 1,1 and wins once he 
# reaches 3, 1
location = 11

# Functions for moving in each direction:
def move_north():
    return 1
def move_south():
    return -1
def move_west():
    return -10
def move_east():
    return 10

# a function that changes the position
def user_direction(user_input, location):
    if user_input.upper() == 'N':
       location += move_north()
    
    elif user_input.upper() == 'S':
        location += move_south()
    
    elif user_input.upper() == 'E':
        location += move_east()
    
    elif user_input.upper() == 'W':
        location += move_west()
    return location

# A function that shows valid direction      
def whereTo(location):
    if location == 11 or location == 21:
        print("You can travel: (N)orth.")
    elif location == 12:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif location == 13:
        print("You can travel: (E)ast or (S)outh.")
    elif location == 23:
        print("You can travel: (E)ast or (W)est.")
    elif location == 22 or location == 33:
        print("You can travel: (S)outh or (W)est.")
    elif location == 32:
        print("You can travel: (N)orth or (S)outh.")
        

whereTo(location)
# A while loop that keeps running while the the location of the player is not 31
# If it reaches 31 that players wins
while location != 31:
    user_input = input('Direction: ')
    prev_location = location
    location = user_direction(user_input, location)
    
    # 11 means 1,1 and so forth
    if location >= 11 and location <= 13 or location >= 21 and location <= 23 or location >= 31 and location <= 33:    
        whereTo(location)

    elif not(location >= 11 and location <= 13 or location >= 21 and location <= 23 or location >= 31 and location <= 33):
        print("Not a valid direction!")
        location = prev_location

else: 
    print("Victory!")