

class Color():
    """makes a color with fields:
    red
    green
    blue
    alpha
    values should be between 0.0 and 1.0 (inclusive), values outside that range will be clipped to the nearest value in the range"""

    def __init__(self, r, g, b, a=1.0):
        self.r = sorted((0, r, 1))[1]
        self.g = sorted((0, g, 1))[1]
        self.b = sorted((0, b, 1))[1]
        self.a = sorted((0, a, 1))[1]
        