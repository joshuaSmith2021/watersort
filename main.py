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
        Tube(4, [SKY, SKY, GREEN, BLUE]),
        Tube(4, [GRAY, OLIVE, PINK, PURPLE]),
        Tube(4, [BROWN, RED, PURPLE, ORANGE]),
        Tube(4, [ORANGE, RED, PINK, ORANGE]),
        Tube(4, [BLUE, YELLOW, RED, GREEN]),
        Tube(4, [GREEN, BROWN, GREEN, YELLOW]),
        Tube(4, [LIME, RED, PURPLE, BROWN]),
        Tube(4, [LIME, PINK, PURPLE, LIME]),
        Tube(4, [BLUE, SKY, GRAY, OLIVE]),
        Tube(4, [OLIVE, GRAY, YELLOW, BROWN]),
        Tube(4, [BLUE, LIME, YELLOW, GRAY]),
        Tube(4, [ORANGE, PINK, SKY, OLIVE]),
        Tube(4, []),
        Tube(4, [])
    ])

    dfs(level.dumps())
