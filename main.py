from watersort import Tube, Level, dfs


if __name__ == '__main__':
    SKY = 0
    YELLOW = 1
    ORANGE = 2
    LIME = 3
    OLIVE = 4
    GREEN = 5
    PURPLE = 6
    RED = 7
    BLUE = 8
    GRAY = 9
    PINK = 10
    BROWN = 11
    UNK = -1

    level = Level([
        Tube(4, [LIME, RED, OLIVE, SKY]),
        Tube(4, [PINK, OLIVE, SKY, SKY]),
        Tube(4, [PURPLE, OLIVE, RED, RED]),
        Tube(4, [GRAY, ORANGE, PINK, BLUE]),
        Tube(4, [PURPLE, GRAY, RED, PINK]),
        Tube(4, [BLUE, PURPLE, GRAY, LIME]),
        Tube(4, [BLUE, OLIVE, PURPLE, ORANGE]),
        Tube(4, [LIME, ORANGE, GRAY, ORANGE]),
        Tube(4, [SKY, BLUE, LIME, PINK]),
        Tube(4, []),
        Tube(4, [])
    ])

    dfs(level.dumps())
