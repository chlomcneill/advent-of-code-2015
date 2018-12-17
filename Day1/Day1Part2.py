def find_floor():
    f = open("/Users/mcneillc/Documents/advent-of-code-2015/Day1/Day1input.txt","r")
    floor_changes = f.readlines()
    f.close()

    position = 0
    current_floor = 0
    for char in floor_changes[0]:
        if char == "(":
            current_floor += 1
            position += 1
            if current_floor < 0:
                return position
        elif char == ")":
            current_floor -= 1
            position += 1
            if current_floor < 0:
                return position
    return current_floor

print(find_floor())
    