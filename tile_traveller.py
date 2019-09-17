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

location += move_west()

while 1.1 <= location <= 1.3 or 2.1 <= location <= 2.3 or 3.1 <= location <= 3.3:
    
else:
    print("invalid direction")
    location = prev_location