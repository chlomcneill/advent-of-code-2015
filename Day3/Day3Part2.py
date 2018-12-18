f = open("/Users/mcneillc/Documents/advent-of-code-2015/Day3/Day3input.txt","r")
directions = f.readlines()
f.close()

def houses_visited():
    santa_journey = directions[0][::2]
    robot_journey = directions[0][1::2]
    locations = [[0,0]]

    santa_x_position = 0
    santa_y_position = 0

    for move in santa_journey:
        if move == "^":
            santa_y_position += 1
            locations.append([santa_x_position, santa_y_position])
        elif move == ">":
            santa_x_position += 1
            locations.append([santa_x_position, santa_y_position])                
        elif move == "v":
            santa_y_position -= 1
            locations.append([santa_x_position, santa_y_position])                
        elif move == "<":
            santa_x_position -= 1
            locations.append([santa_x_position, santa_y_position]) 

    robot_x_position = 0
    robot_y_position = 0

    for move in robot_journey:
        if move == "^":
            robot_y_position += 1
            locations.append([robot_x_position, robot_y_position])
        elif move == ">":
            robot_x_position += 1
            locations.append([robot_x_position, robot_y_position])                
        elif move == "v":
            robot_y_position -= 1
            locations.append([robot_x_position, robot_y_position])                
        elif move == "<":
            robot_x_position -= 1
            locations.append([robot_x_position, robot_y_position]) 

    houses = []
    for coord in locations:
        if coord not in houses:
            houses.append(coord)

    return len(houses)

print(houses_visited())