from circle_stats import has_intersection
from circles_intersection_draw import draw_data


circle_1 = {"x": 0, "y": 0, "r": 2}
circle_2 = {"x": 3, "y": 0, "r": 1}

result = has_intersection(circle_1, circle_2)

print(result)

if result["is_intersection"]:
    if result["intersections_count"] == 1:
        print("Kruznice se protinaji a maji 1 prunik.")
    elif result["intersections_count"] == 2:
        print("Kruznice se protinaji a maji 2 pruniky.")
else:
    print("Kruznice se neprotinaji a maji 0 pruniku.")

draw_data(circle_1, circle_2)
