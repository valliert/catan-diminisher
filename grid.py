import matplotlib.pyplot as pplt
import matplotlib.patches as patches
import math
import hex
import random

class Grid:
    fig, ax = pplt.subplots()
    ax.set_axis_off()

    terrains = list('mmmhhhffffppppFFFF')
    vals = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
    vertices = list(range(54))
    hex_adjacency_list = {
           0:[3, 4], 
           1:[4, 5], 
           2:[5, 6], 
           3:[0, 7], 
           4:[0, 1, 8], 
           5:[1, 2, 9], 
           6:[2, 10], 
           7:[3, 11, 12], 
           8:[4, 12, 13], 
           9:[5, 13, 14], 
           10:[6, 14, 15], 
           11:[7 ,16], 
           12:[7, 8, 17], 
           13:[8, 9, 18],
           14:[9, 10, 19], 
           15:[10, 20], 
           16:[11, 21, 22], 
           17:[12, 22, 23], 
           18:[13, 23, 24], 
           19:[14, 24, 25],
           20:[15, 25, 26], 
           21:[16, 27], 
           22:[16, 17, 28], 
           23:[17, 18, 29], 
           24:[18, 19, 30], 
           25:[19, 20, 31], 
           26:[20, 32], 
           27:[21, 33], 
           28:[22, 33, 34], 
           29:[23, 34, 35], 
           30:[24, 35, 36], 
           31:[25, 36, 37], 
           32:[26, 37], 
           33:[27, 28, 38], 
           34:[28, 29, 39], 
           35:[29, 30, 40], 
           36:[30, 31, 41], 
           37:[31, 32, 42], 
           38:[33, 43], 
           39:[34, 43, 44], 
           40:[35, 44, 45], 
           41:[36, 45, 46], 
           42:[37, 46], 
           43:[38, 39, 47], 
           44:[39, 40, 48], 
           45:[40, 41, 49], 
           46:[41, 42, 50], 
           47:[43, 51], 
           48:[44, 51, 52], 
           49:[45, 52, 53], 
           50:[56, 53], 
           51:[47, 48], 
           52:[48, 49], 
           53:[49, 50]
    }
    vertex_coords = []
    vertex_coords.extend([(2*i*r + 3*r, 8 - 0.0) for i in range(3)])
    vertex_coords.extend([(2*i*r + 2*r, 8 - 0.5) for i in range(4)])
    vertex_coords.extend([(2*i*r + 2*r, 8 - 1.5) for i in range(4)])
    vertex_coords.extend([(2*i*r + 1*r, 8 - 2.0) for i in range(5)])
    vertex_coords.extend([(2*i*r + 1*r, 8 - 3.0) for i in range(5)])
    vertex_coords.extend([(2*i*r + 0*r, 8 - 3.5) for i in range(6)])
    vertex_coords.extend([(2*i*r + 0*r, 8 - 4.5) for i in range(6)])
    vertex_coords.extend([(2*i*r + 1*r, 8 - 5.0) for i in range(5)])
    vertex_coords.extend([(2*i*r + 1*r, 8 - 6.0) for i in range(5)])
    vertex_coords.extend([(2*i*r + 2*r, 8 - 6.5) for i in range(4)])
    vertex_coords.extend([(2*i*r + 2*r, 8 - 7.5) for i in range(4)])
    vertex_coords.extend([(2*i*r + 3*r, 8 - 8.0) for i in range(3)])
    

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
        

    

    def draw_new_map(players, randomize=True):
        terrain_list = random.sample(Grid.terrains, len(Grid.terrains))
        val_list = random.sample(Grid.vals, len(Grid.vals))
        hexes = [hex.Hex(val, terrain) for val, terrain in zip(val_list, terrain_list)] #Add terrain hexes
        hexes.append(hex.Hex(0, 'd'))                                                   #Add desert hex
        random.shuffle(hexes)                                                           #Randomize the board. I have not implemented the "standard" setup

        R = 1
        r=math.sqrt(3)/2*R
        Grid.ax.set_xlim(0 - 0.5, 15*r + 0.5)
        Grid.ax.set_ylim(0 - 0.5, 8*R + 0.5)
        Grid.fig.set_facecolor("blue")
        Grid.fig.set_size_inches(12, 8)

        Grid.draw_all_rows(hexes)


       

        

        
        for i, (x, y) in zip(Grid.vertices, Grid.vertex_coords):
            vertex = pplt.Circle((x, y), radius=0.25, color='red', fill=True)
            Grid.ax.add_patch(vertex)
            pplt.text(x, y, str(i), horizontalalignment='center', verticalalignment='center')





        pplt.show()
       


Grid().draw_new_map(None)