import grid as g
import player as p
import hex as h
import matplotlib.pyplot as pplt
import itertools

grid = g.Grid()
hexes = grid.get_new_hexes()

players = [p.Player(color) for color in ["red", "blue", "purple", "orange"]]

def get_best_n_vertices(n):
    best = []
    for vertex, hex_list in sorted(grid.vertex_hex_adjacency_list.items(), key = (lambda pair: sum(hex.pips for hex in pair[1])), reverse=True):
        if grid.owned_vertices[vertex] == 0:
            best.append((vertex, sum(hex.pips for hex in hex_list)))
        if len(best) == n:
            return best
    return best
def propose_vertex(player: p.Player, vertex: int):
    grid.player_owned_vertices[vertex] = player.color
    for adj_vertex in grid.vertex_adjacency_list[vertex]:
        grid.player_owned_vertices[adj_vertex] = "black"


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

def main():
    while len(players) > 0:
        best_vertices = get_best_n_vertices(8)
        pair = None
        player = players[0]
        pair_ranking = sorted(itertools.combinations(best_vertices, 2), key = lambda x: x[0][1] + x[1][1])
        for i in range(len(pair_ranking)):
            pair = pair_ranking[i]
            value = pair[0][1] + pair[1][1]
            if value < sum(pips for _, pips in best_vertices) / 4 and not pair[1][0] in grid.vertex_adjacency_list[pair[0][0]]:
                pair = (pair_ranking[i-1][0][0], pair_ranking[i-1][1][0])
                break
        claim_vertex(player, pair[0])
        claim_vertex(player, pair[1])
        players.remove(player)
        grid.draw_map(hexes)
        pplt.pause(1)




    # for player in players:
    #     max = None
    #     max_vert = None
    #     for i in range(len(grid.owned_vertices)):
    #         if grid.owned_vertices[i] == 0:
    #             value = player.valuation_function(grid.vertex_hex_adjacency_list[i])
    #             if max is None or value > max:
    #                 max = value
    #                 max_vert = i
    #     claim_vertex(player, max_vert)
    #     grid.draw_map(hexes)
    #     pplt.pause(1)
        
    # for player in reversed(players):
    #     max = None
    #     max_vert = None
    #     for i in range(len(grid.owned_vertices)):
    #         if grid.owned_vertices[i] == 0:
    #             value = player.valuation_function(grid.vertex_hex_adjacency_list[i])
    #             if max is None or value > max:
    #                 max = value
    #                 max_vert = i
    #     claim_vertex(player, max_vert)
    #     grid.draw_map(hexes)
    #     pplt.pause(1)
    pplt.show()

main()