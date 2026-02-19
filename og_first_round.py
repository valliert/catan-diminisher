import grid as g
import player as p
import hex as h

grid = g.Grid()
hexes = grid.get_new_hexes()

players = [p.Player(color) for color in ["red", "blue", "purple", "gray"]]

def claim_vertex(player: p.Player, vertex: int):
    grid.player_owned_vertices[vertex] = player.color
    grid.owned_vertices[vertex] = 1
    for adj_vertex in grid.vertex_adjacency_list[vertex]:
        grid.player_owned_vertices[adj_vertex] = "black"
        grid.owned_vertices[adj_vertex] = 1

for player in players:
    max = None
    for i in range(len(grid.owned_vertices)):
        if grid.owned_vertices[i] == 0:
            value = player.valuation_function()
