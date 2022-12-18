import turtle

inch = 20  # pixels
map_size = (48, 48)  # in inches 860x860

river = "R"
rock = "X"
treasure = "T"
player = "P"
member = "M"
enemy = "E"

TEST_MAP = """
XXXXXXXXXX
X  E M E X
X E E E EX
X E   RR X
X   RRR  X
XRRRR    X
X        X
X        X
X E  E TEX
X ET    EX
X E  P  EX
XXXXXXXXXX
"""

map_1 = """
RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
R                                               R
RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
"""

col = map_size[0]
ro = map_size[1]


# print(rows, columns)

