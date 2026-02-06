import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

fig, ax = plt.subplots()

hexes = []
def draw_row(x_i, y, n, ax=ax, R=1):
    r=math.sqrt(3)/2*R
    x = x_i
    for _ in range(n):
        hex = patches.RegularPolygon((x*r, y*R), 6, radius=R, edgecolor='blue')
        ax.add_patch(hex)
        print(hex)
        x+=2
def draw_map(ax=ax, R=1):
    r=math.sqrt(3)/2*R
    ax.set_xlim(0, 10*r)
    ax.set_ylim(0, 8*R)
    draw_row(3, 7, 3)
    draw_row(2, 5.5, 4)
    draw_row(1, 4, 5)
    draw_row(2, 2.5, 4)
    draw_row(3, 1, 3)

draw_map()
plt.show()