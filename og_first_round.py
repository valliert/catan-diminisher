import grid as g
import player as p
import hex as h
import matplotlib.pyplot as pplt

grid = g.Grid()
hexes = grid.get_new_hexes()

players = [p.Player(color) for color in ["red", "blue", "purple", "orange"]]

def claim_vertex(player: p.Player, vertex: int):
    grid.player_owned_vertices[vertex] = player.color
    grid.owned_vertices[vertex] = 1

    v_1, v_2 = player.owned_pair
    if v_1 == -1:
        v_1 = vertex
    else:
        v_2 = vertex
    player.owned_pair = (v_1, v_2)

    for adj_vertex in grid.vertex_adjacency_list[vertex]:
        grid.player_owned_vertices[adj_vertex] = "black"
        grid.owned_vertices[adj_vertex] = 1
    grid.add_text(f"Player {player.color} claimed vertex {vertex}. \n    New pair: {player.owned_pair}\n    Value:{player.valuation_function(grid.vertex_hex_adjacency_list[v_1]) + player.valuation_function(grid.vertex_hex_adjacency_list[v_2]) }")

for player in players:
    max = None
    max_vert = None
    for i in range(len(grid.owned_vertices)):
        if grid.owned_vertices[i] == 0:
            value = player.valuation_function(grid.vertex_hex_adjacency_list[i])
            if max is None or value > max:
                max = value
                max_vert = i
    claim_vertex(player, max_vert)
    grid.draw_map(hexes)
    pplt.pause(1)
    
for player in reversed(players):
    max = None
    max_vert = None
    for i in range(len(grid.owned_vertices)):
        if grid.owned_vertices[i] == 0:
            value = player.valuation_function(grid.vertex_hex_adjacency_list[i])
            if max is None or value > max:
                max = value
                max_vert = i
    claim_vertex(player, max_vert)
    grid.draw_map(hexes)
    pplt.pause(1)
pplt.show()