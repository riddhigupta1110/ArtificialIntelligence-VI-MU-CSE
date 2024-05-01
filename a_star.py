def generate_child(data, level, direction):
    """ Generate child nodes from the given node by moving the blank space
        either in the four directions {up,down,left,right} """
    def shuffle(puz, x1, y1, x2, y2):
        """ Move the blank space in the given direction and if the position value are out
            of limits the return None """
        if 0 <= x2 < len(data) and 0 <= y2 < len(data):
            temp_puz = [row[:] for row in puz]
            temp_puz[x2][y2], temp_puz[x1][y1] = temp_puz[x1][y1], temp_puz[x2][y2]
            return temp_puz
        else:
            return None

    x, y = find(data, '_')
    """ val_list contains position values for moving the blank space in either of
        the 4 directions [up,down,left,right] respectively. """
    val_list = [[x, y - 1, "LEFT"], [x, y + 1, "RIGHT"], [x - 1, y, "UP"], [x + 1, y, "DOWN"]]
    children = []
    for i in val_list:
        child = shuffle(data, x, y, i[0], i[1])
        if child is not None:
            children.append((child, level + 1, i[2]))
    return children

def find(puz, x):
    """ Specifically used to find the position of the blank space """
    for i, row in enumerate(puz):
        for j, val in enumerate(row):
            if val == x:
                return i, j

def h(start, goal):
    """ Calculates the different between the given puzzles """
    return sum(1 for i in range(len(start)) for j in range(len(start)) if start[i][j] != goal[i][j] and start[i][j] != '_')

def f(start, goal, level):
    """ Calculates the f value """
    return level + h(start, goal)

def process(size):
    """ Accept Start and Goal Puzzle state"""
    def print_puzzle(puz):
        for row in puz:
            print(' '.join(row))
        print()

    print("Enter the start state matrix ")
    start = [input().split() for _ in range(size)]
    print("Enter the goal state matrix")
    goal = [input().split() for _ in range(size)]
    start_node = (start, 0, None)
    open_list = [start_node]
    closed_list = []
    print("\n\n")
    while True:
        cur = open_list[0]
        if cur[2]:  # Avoid printing action for the start state
            print("Action taken:", cur[2])
        print("f value:", f(cur[0], goal, cur[1]))
        print_puzzle(cur[0])
        if h(cur[0], goal) == 0:
            break
        for child in generate_child(*cur):
            open_list.append(child)
        closed_list.append(cur)
        del open_list[0]
        open_list.sort(key=lambda x: f(x[0], goal, x[1]))

process(3)