f = open("/Users/mcneillc/Documents/advent-of-code-2015/Day3/Day3input.txt","r")
directions = f.readlines()
f.close()

def houses_visited_at_least_once():
    x_position = 0
    y_position = 0
    locations = [[0,0]]

    for char in directions[0]:
        if char == "^":
            y_position += 1
            locations.append([x_position, y_position])
        elif char == ">":
            x_position += 1
            locations.append([x_position, y_position])                
        elif char == "v":
            y_position -= 1
            locations.append([x_position, y_position])                
        elif char == "<":
            x_position -= 1
            locations.append([x_position, y_position]) 

    houses = []
    for coord in locations:
        if coord not in houses:
            houses.append(coord)

    return len(houses)

print(houses_visited_at_least_once())