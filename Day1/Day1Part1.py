def find_floor():
    f = open("/Users/mcneillc/Documents/advent-of-code-2015/Day1/Day1input.txt","r")
    floor_changes = f.readlines()
    f.close()

    current_floor = 0
    for char in floor_changes[0]:
        if char == "(":
            current_floor += 1
        elif char == ")":
            current_floor -= 1
    return current_floor

print(find_floor())
    