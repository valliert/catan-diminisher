import matplotlib.pyplot as pplt
import matplotlib.patches as patches
import math
import hex
import random

class Grid:
    fig, ax = pplt.subplots()

    terrains = list('mmmhhhffffppppFFFF')
    vals = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
    

    def draw_row(x_i, y, hexes: list[hex.Hex], ax=ax, R=1):
        r=math.sqrt(3)/2*R
        x = x_i
        for hex in hexes:
            patch = patches.RegularPolygon((x*r, y*R), 6, radius=R, facecolor=hex.color, edgecolor='black')
            ax.add_patch(patch)
            pplt.text(x*r, y*R, str(hex.die_value) + "\n" + "o"*hex.pips, horizontalalignment='center', verticalalignment='center')
            x+=2
    def draw_all_rows(hexes):
        Grid.draw_row(3, 7, hexes[:3])
        Grid.draw_row(2, 5.5, hexes[3:7])
        Grid.draw_row(1, 4, hexes[7:12])
        Grid.draw_row(2, 2.5, hexes[12:16])
        Grid.draw_row(3, 1, hexes[16:19])
        pplt.show()

    def draw_new_map(randomize=True):
        terrain_list = random.sample(Grid.terrains, len(Grid.terrains))
        val_list = random.sample(Grid.vals, len(Grid.vals))
        hexes = [hex.Hex(val, terrain) for val, terrain in zip(val_list, terrain_list)]
        hexes.append(hex.Hex(0, 'd'))
        random.shuffle(hexes)

        R = 1
        r=math.sqrt(3)/2*R
        Grid.ax.set_xlim(0, 10*r)
        Grid.ax.set_ylim(0, 8*R)

        Grid.draw_all_rows(hexes)



        

Grid().draw_new_map()