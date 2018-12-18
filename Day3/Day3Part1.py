f = open("/Users/mcneillc/Documents/advent-of-code-2015/Day3/Day3input.txt","r")
directions = f.readlines()
f.close()

def houses_visited():
    journey = directions[0]
    locations = [[0,0]]

    x_position = 0
    y_position = 0

    for move in journey:
        if move == "^":
            y_position += 1
            locations.append([x_position, y_position])
        elif move == ">":
            x_position += 1
            locations.append([x_position, y_position])                
        elif move == "v":
            y_position -= 1
            locations.append([x_position, y_position])                
        elif move == "<":
            x_position -= 1
            locations.append([x_position, y_position]) 

    houses = []
    for coord in locations:
        if coord not in houses:
            houses.append(coord)

    return len(houses)

print(houses_visited())