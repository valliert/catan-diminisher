class Hex:
    def val_to_pips(val):
        if 1 < val < 7:
            return val - 1
        elif 7 < val < 13:
            return 13 - val
        else:
            return 0
    terrain_resource_dict = {'m': 'ore',    #mountains
                             'f': 'grain',  #fields
                             'h': 'brick',  #hills
                             'p': 'wool',   #pastures
                             'F': 'lumber', #Forest
                             's': None,     #sea
                             'd': None}     #desert
    terrain_color_dict = {'m': 'gray',
                             'f': 'yellow',
                             'h': 'maroon',
                             'p': 'lime',
                             'F': 'green',
                             's': 'blue',
                             'd': 'black'}

    def __init__(self, die_value, terrain) -> None:
        self.die_value = die_value
        self.pips = Hex.val_to_pips(die_value)
        self.terrain = terrain
        self.resource = Hex.terrain_resource_dict[terrain]
        self.color = Hex.terrain_color_dict[terrain]

    def get_short_resource(self):
        return self.terrain[0]


