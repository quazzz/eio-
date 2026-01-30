# Read input
n = int(input())
defenders = []
for _ in range(n):
    x, y = map(int, input().split())
    defenders.append((x, y))

att_x, att_y = map(int, input().split())
goal_x, goal_y = map(int, input().split())

found_offside = False

all_x = [d[0] for d in defenders] + [att_x, goal_x]
for line_x in all_x:
    att_left = att_x < line_x
    goal_left = goal_x < line_x
    
    if att_left == goal_left:  # Both on same side
        defenders_same_side = sum(1 for d in defenders if (d[0] < line_x) == att_left)
        if defenders_same_side <= 1:
            found_offside = True
            break

# Try all possible horizontal lines (at each y-coordinate)
if not found_offside:
    all_y = [d[1] for d in defenders] + [att_y, goal_y]
    for line_y in all_y:
        # Try line below: y < line_y
        att_below = att_y < line_y
        goal_below = goal_y < line_y
        
        if att_below == goal_below:  # Both on same side
            defenders_same_side = sum(1 for d in defenders if (d[1] < line_y) == att_below)
            if defenders_same_side <= 1:
                found_offside = True
                break

if found_offside:
    print("JAH")
else:
    print("EI")