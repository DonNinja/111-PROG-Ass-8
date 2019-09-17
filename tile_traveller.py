# Create a game a game that consist of a 3x3 grid
# Where the player can only move in a fixed direction
# based on the tile he's at
# The player starts at tile 1,1 and wins once he 
# reaches 3, 1
location = 1.1

def move_north():
    return .1
def move_south():
    return -.1
def move_west():
    return -1
def move_east():
    return 1


def user_direction(user_input, location):
    if user_input.upper == 'N':
       location += move_north()
    
    elif user_input.upper == 'S':
        location += move_south()
    
    elif user_input.upper == 'E':
        location += move_east()
    
    elif user_input.upper == 'W':
        location += move_west()
    return location
        
def whereTo(location):
    if location == 1.1 or location == 2.1:
        print("You can travel (N)orth")
    elif location == 1.2:
        print("You can travel (N)orth or (E)ast or (S)outh")
    elif location == 1.3:
        print("You can travel (E)ast or (S)outh")
    elif location == 2.3:
        print("You can travel (E)ast or (W)est")
    elif location == 2.2 or location == 3.3:
        print("You can travel (S)outh or (W)est")
    elif location == 3.2:
        print("You can travel (N)orth or (S)outh")
        
print(location)

while location >= 1.1 and location <= 1.3 or location >= 2.1 and location <= 2.3 or location >= 3.1 and location <= 3.3:
    whereTo(location)
    user_input = input('Direction: ')
    prev_location = location
    print(user_direction(user_input, location))
    location = user_direction(user_input, location)
    


else:
    print("invalid direction")
    location = prev_location