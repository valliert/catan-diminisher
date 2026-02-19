import hex as h
class Player:
    def default_valuation(adjacent_hexes: list[h.Hex]):
        value = 0
        for hex in adjacent_hexes:
            value += hex.pips
        return value
    def __init__(self, color) -> None:
        self.valuation_function = Player.default_valuation
        self.color = color
        self.owned_pair: tuple[int, int]
