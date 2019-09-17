# Create a game a game that consist of a 3x3 grid
# Where the player can only move in a fixed direction
# based on the tile he's at
# The player starts at tile 1,1 and wins once he 
# reaches 3, 1
location = 11

def move_north():
    return 1
def move_south():
    return -1
def move_west():
    return -10
def move_east():
    return 10


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
        
def whereTo(location):
    if location == 11 or location == 21:
        print("You can travel (N)orth")
    elif location == 12:
        print("You can travel (N)orth or (E)ast or (S)outh")
    elif location == 13:
        print("You can travel (E)ast or (S)outh")
    elif location == 23:
        print("You can travel (E)ast or (W)est")
    elif location == 22 or location == 33:
        print("You can travel (S)outh or (W)est")
    elif location == 32:
        print("You can travel (N)orth or (S)outh")
        
print(location)

while location != 31:
    user_input = input('Direction: ')
    prev_location = location
    if location >= 10 and location <= 13 or location >= 21 and location <= 23 or location >= 31 and location <= 33:
        whereTo(location)
        print(user_direction(user_input, location))
        location = user_direction(user_input, location)
    if not(location >= 10 and location <= 13 or location >= 21 and location <= 23 or location >= 31 and location <= 33):
        print("invalid direction")
        location = prev_location