class Setup:

    level = 1

    # map/window size
    WIDTH = 5000
    HEIGHT = 800

    # game_speed
    GAME_SPEED = 1
    FRAME_SPEED = "fastest"
    MELEE = 10  # melee distance

    # map borders
    OUTLINE_THICKNESS = 5
    OUTLINE_TOP = int(HEIGHT / 2), int(HEIGHT / 2) + OUTLINE_THICKNESS
    OUTLINE_BOTTOM = 0 - int(HEIGHT / 2) - OUTLINE_THICKNESS, 0 - int(HEIGHT / 2)
    OUTLINE_RIGHT = int(WIDTH / 2), int(WIDTH / 2) + OUTLINE_THICKNESS
    OUTLINE_LEFT = 0 - int(WIDTH / 2) - OUTLINE_THICKNESS, 0 - int(WIDTH / 2)
    OUTLINE = [OUTLINE_TOP, OUTLINE_BOTTOM, OUTLINE_RIGHT, OUTLINE_LEFT]
