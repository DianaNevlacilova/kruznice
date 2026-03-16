import matplotlib.pyplot as plt


def draw_data(circle_1, circle_2):
    fig, ax = plt.subplots()

    c1 = plt.Circle((circle_1["x"], circle_1["y"]), circle_1["r"], fill=False)
    c2 = plt.Circle((circle_2["x"], circle_2["y"]), circle_2["r"], fill=False)

    ax.add_patch(c1)
    ax.add_patch(c2)

    ax.set_aspect("equal")

    min_x = min(circle_1["x"] - circle_1["r"], circle_2["x"] - circle_2["r"]) - 1
    max_x = max(circle_1["x"] + circle_1["r"], circle_2["x"] + circle_2["r"]) + 1
    min_y = min(circle_1["y"] - circle_1["r"], circle_2["y"] - circle_2["r"]) - 1
    max_y = max(circle_1["y"] + circle_1["r"], circle_2["y"] + circle_2["r"]) + 1

    ax.set_xlim(min_x, max_x)
    ax.set_ylim(min_y, max_y)

    plt.grid(True)
    plt.show()