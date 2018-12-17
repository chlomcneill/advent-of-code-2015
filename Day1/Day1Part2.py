f = open("/Users/mcneillc/Documents/advent-of-code-2015/Day1/Day1input.txt","r")
floor_changes = f.readlines()
f.close()

def find_first_time_to_enter_basement():
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

print(find_first_time_to_enter_basement())
    