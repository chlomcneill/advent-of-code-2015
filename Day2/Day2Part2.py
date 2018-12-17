f = open("/Users/mcneillc/Documents/advent-of-code-2015/Day2/Day2input.txt","r")
present_measurements = f.readlines()
f.close()

present_measurements = [line[:-1].split('x') for line in present_measurements]

def ribbon_needed_for_1_present(l, w, h):
    sides = [l, w, h]
    sides.sort()
    ribbon_needed = 2*(sides[0]+sides[1]) + (l * w * h)
    return ribbon_needed

def find_all_ribbon_needed():
    total_ribbon_needed = 0
    for present in present_measurements:
        l = int(present[0])
        w = int(present[1])
        h = int(present[2])
        total_ribbon_needed += ribbon_needed_for_1_present(l,w,h)
    return total_ribbon_needed

print(find_all_ribbon_needed())