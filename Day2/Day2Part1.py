f = open("/Users/mcneillc/Documents/advent-of-code-2015/Day2/Day2input.txt","r")
present_measurements = f.readlines()
f.close()

present_measurements = [line[:-1].split('x') for line in present_measurements]

def paper_needed_for_1_present(l, w, h):
    sides = [l, w, h]
    sides.sort()
    smallest_face = sides[0] * sides[1]
    paper_needed = 2*(l*w + l*h + h*w) + smallest_face
    return paper_needed

def find_all_paper_needed():
    total_paper_needed = 0
    for present in present_measurements:
        l = int(present[0])
        w = int(present[1])
        h = int(present[2])
        total_paper_needed += paper_needed_for_1_present(l,w,h)
    return total_paper_needed

print(find_all_paper_needed())
