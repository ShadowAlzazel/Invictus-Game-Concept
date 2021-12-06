hex_coordinate_index = 29
length = 5
width = 5

if not (hex_coordinate_index + 1) % length == 0:
    print('Can move Right')
else:
    print('Cannot move Right')

if not hex_coordinate_index % length == 0:
    print('Can Move Left')
else: 
    print("Cannot move Left")

if not (hex_coordinate_index >= length * (width - 1)) and not ((hex_coordinate_index // length) % 2 == 1 and (hex_coordinate_index + 1) % length == 0):
    print('Can Move Upright')
else: 
    print("Cannot move upright")

if not (hex_coordinate_index) >= length * (width - 1) and not((hex_coordinate_index // length) % 2 == 0 and hex_coordinate_index % length == 0):
    print('Can Move Upleft')
else: 
    print("Cannot move upleft")

if not (hex_coordinate_index) // length == 0 and not ((hex_coordinate_index // length) % 2 == 1 and (hex_coordinate_index + 1) % length == 0):
    print('Can Move downright')
else: 
    print("Cannot move downright")

if not (hex_coordinate_index) // length == 0 and not ((hex_coordinate_index // length) % 2 == 0 and hex_coordinate_index % length == 0):
    print('Can Move downleft')
else: 
    print("Cannot move downleft")