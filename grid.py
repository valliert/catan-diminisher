import matplotlib.pyplot as pplt
import matplotlib.patches as patches
import math
import hex as h
import random

class Grid:
    
    R = 1
    r=math.sqrt(3)/2*R
    terrains = list('mmmhhhffffppppFFFF')
    vals = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
    
    vertex_indices = list(range(54))
    hex_indices = list(range(19))
    hex_top_indices = [0, 1, 2, 7, 8, 9, 10, 16, 17, 18, 19, 20, 28, 29, 30, 31, 39, 40, 41]
    vertex_adjacency_list = { #Hard-coded list, but it's fine. Will never change within the scope of this project since the board from the base game will suffice (no Seafarers or anything like that)
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
    def __init__(self) -> None:
        self.info_text: pplt.Text = None
        self.fig, self.ax = pplt.subplots()
        self.ax.set_axis_off()
        self.player_owned_vertices = ["white"] * 54 #Owner of each index
        self.owned_vertices = [0] * 54 #If index has been assigned. !White and 0 signifies 'proposed but not yet assigned'
        self.vertex_hex_adjacency_list: dict[int, list[h.Hex]] = {-1: []}
        
        #Visual coordinates for each vertex
        Grid.vertex_coords.extend([(2*i*Grid.r + 3*Grid.r, 8 - 0.0) for i in range(3)])
        Grid.vertex_coords.extend([(2*i*Grid.r + 2*Grid.r, 8 - 0.5) for i in range(4)])
        Grid.vertex_coords.extend([(2*i*Grid.r + 2*Grid.r, 8 - 1.5) for i in range(4)])
        Grid.vertex_coords.extend([(2*i*Grid.r + 1*Grid.r, 8 - 2.0) for i in range(5)])
        Grid.vertex_coords.extend([(2*i*Grid.r + 1*Grid.r, 8 - 3.0) for i in range(5)])
        Grid.vertex_coords.extend([(2*i*Grid.r + 0*Grid.r, 8 - 3.5) for i in range(6)])
        Grid.vertex_coords.extend([(2*i*Grid.r + 0*Grid.r, 8 - 4.5) for i in range(6)])
        Grid.vertex_coords.extend([(2*i*Grid.r + 1*Grid.r, 8 - 5.0) for i in range(5)])
        Grid.vertex_coords.extend([(2*i*Grid.r + 1*Grid.r, 8 - 6.0) for i in range(5)])
        Grid.vertex_coords.extend([(2*i*Grid.r + 2*Grid.r, 8 - 6.5) for i in range(4)])
        Grid.vertex_coords.extend([(2*i*Grid.r + 2*Grid.r, 8 - 7.5) for i in range(4)])
        Grid.vertex_coords.extend([(2*i*Grid.r + 3*Grid.r, 8 - 8.0) for i in range(3)])
    

    def draw_row(self, x_i, y, hexes: list[h.Hex]):
        R = Grid.R
        r = Grid.r
        x = x_i
        for hex in hexes:
            patch = patches.RegularPolygon((x*r, y*R), 6, radius=R, facecolor=hex.color, edgecolor='black')
            self.ax.add_patch(patch)
            pplt.text(x*r, y*R, str(hex.die_value) + "\n" + "o"*hex.pips, horizontalalignment='center', verticalalignment='center')
            x+=2
    def draw_all_rows(self, hexes):
        self.draw_row(3, 7, hexes[:3])
        self.draw_row(2, 5.5, hexes[3:7])
        self.draw_row(1, 4, hexes[7:12])
        self.draw_row(2, 2.5, hexes[12:16])
        self.draw_row(3, 1, hexes[16:19])
        
    def get_new_hexes(self):
        terrain_list = random.sample(Grid.terrains, len(Grid.terrains))
        val_list = random.sample(Grid.vals, len(Grid.vals))
        hexes = [h.Hex(val, terrain) for val, terrain in zip(val_list, terrain_list)] #Add terrain hexes
        hexes.append(h.Hex(0, 'd'))                                                   #Add desert hex
        random.shuffle(hexes) #Randomize the board. I have not implemented the "standard" setup

        for i in range(len(Grid.hex_top_indices)): #Establish Vertex-Hex adjacencies
            num_vertices = [] #Distances between vertices 0-1, 3-4, and 5-6 for the row
            index = Grid.hex_top_indices[i]
            match index:
                case n if 0 <= n < 7:
                    num_vertices=[3, 3, 4]
                case n if 7 <= n < 16:
                    num_vertices=[4, 4, 5]
                case n if 16 <= n < 28:
                    num_vertices=[5, 5, 5]
                case n if 0 <= n < 39:
                    num_vertices=[5, 4, 4]
                case n if 39 <= n < 54:
                    num_vertices=[4, 3, 3]
                
            adjacent_vertices = [index, 
                                index + num_vertices[0], 
                                index + num_vertices[0] + 1,
                                index + num_vertices[0] + 1 + num_vertices[1],
                                index + num_vertices[0] + 1 + num_vertices[1] + 1,
                                index + num_vertices[0] + 1 + num_vertices[1] + 1 + num_vertices[2]]
            for vertex in adjacent_vertices:
                v_list = self.vertex_hex_adjacency_list.get(vertex)
                if v_list is not None:
                    v_list.append(hexes[i])
                    self.vertex_hex_adjacency_list[vertex] = v_list
                else:
                    self.vertex_hex_adjacency_list[vertex] = [hexes[i]]
        return hexes
    

    def draw_map(self, hexes, randomize=True):                                                         
        R = Grid.R
        r = Grid.r
        self.ax.set_xlim(0 - 0.5, 20*r + 0.5)
        self.ax.set_ylim(0 - 0.5, 8*R + 0.5)
        self.fig.set_facecolor("blue")
        self.fig.set_size_inches(16, 8)

        self.draw_all_rows(hexes)
        
        for i, (x, y) in zip(Grid.vertex_indices, Grid.vertex_coords):
            ring = pplt.Circle((x, y), radius=0.25, facecolor=self.player_owned_vertices[i], edgecolor="black", fill=True)
            fill = pplt.Circle((x, y), radius=0.16, facecolor=self.player_owned_vertices[i] if self.owned_vertices[i] else "white", fill=True)
            self.ax.add_patch(ring)
            self.ax.add_patch(fill)
            pplt.text(x, y, str(i), horizontalalignment='center', verticalalignment='center')



        #INFO TEXT SETUP
    def add_text(self, text: str, overwrite=False):
        if self.info_text is None:
            self.info_text = pplt.text(10, 9.5, text, 
                fontsize=8, 
                bbox=dict(facecolor='white', alpha=1, boxstyle='round,pad=0.5'), verticalalignment='top')
        elif overwrite:
            self.info_text.remove()
            self.info_text = pplt.text(10, 9.5, text, 
                fontsize=8, 
                bbox=dict(facecolor='white', alpha=1, boxstyle='round,pad=0.5'), verticalalignment='top')
        else:
            new_text = self.info_text.get_text() + "\n" + text
            self.info_text.remove()
            self.info_text = pplt.text(10, 9.5, new_text, 
                fontsize=8, 
                bbox=dict(facecolor='white', alpha=1, boxstyle='round,pad=0.5'), verticalalignment='top')
        


        # pplt.show(block=False)
       

# grid = Grid()
# grid.draw_map(grid.get_new_hexes())