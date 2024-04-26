from collections import OrderedDict

def execute_action(action):
    global clear, on, on_table, hand, current
    if action[0] == 'ON':
        # ON 1 2 => 1 on 2
        if action[1] + '*' + action[2] in on:
            return
        else:
            # Ensure that block 2 is clear
            execute_action(['CLEAR', action[2]])
            # Ensure block 1 is held
            execute_action(['HOLD', action[1]])
            print('Stack', action[1], action[2])
            clear[action[2]] = None
            clear[action[1]] = None
            on[action[1] + '*' + action[2]] = None
            hand = None

    elif action[0] == 'CLEAR':
        # CLEAR 1 => no block on top
        if action[1] in clear:
            return
        else:
            a = action[1]
            b = None
            for item in on:
                if a == item[2]:
                    b = item[0]
                    break
            if b is None:
                return
            execute_action(['CLEAR', b])
            execute_action(['ON', b, a])
            execute_action(['HANDEMPTY'])
            hand = b
            clear[a] = None
            clear[b] = None
            on_table[a] = None
            on.pop(b + '*' + a)
            print('Unstack', b , a)
            
    elif action[0] == 'HANDEMPTY':
        if hand is None:
            return
        else:
            print('Putdown', hand)
            on_table[hand] = None
            hand = None

    elif action[0] == 'ONTABLE':
        if action[1] in on_table:
            return
        else:
            a = action[1]
            b = None
            for item in on:
                if a == item[2]:
                    b = item[0]
                    break
            if b is None:
                return
            execute_action(['CLEAR', b])
            execute_action(['ON', b, a])
            execute_action(['HANDEMPTY'])
            hand = b
            clear[a] = None
            clear[b] = None
            on_table[a] = None
            on.pop(b + '*' + a)
            print('Unstack', b , a)

    elif action[0] == 'HOLD':
        if hand == action[1]:
            return
        else:
            execute_action(["CLEAR", action[1]])
            execute_action(["ONTABLE", action[1]])
            execute_action(["HANDEMPTY"])
            hand = action[1]
            on_table.pop(hand)
            print("PickUp", hand)
    
    # Update current state and print it
    current = []
    for block in on_table:
        current.append([block])
    for pair in on:
        current[-1].append(pair.split('*')[0])
    current.reverse()
    for sublist in current:
        sublist.reverse()
    # print("Current state:", current, end='\n\n')
    hierarchy_levels = []
    # Iterate through the current state to identify hierarchical levels
    for sublist in current:
        for i, block in enumerate(sublist):
            # Ensure the hierarchy_levels list is long enough
            if len(hierarchy_levels) <= i:
                hierarchy_levels.append([])
            hierarchy_levels[i].append(block)

    # Print the hierarchical levels
    print("Current state:")
    for level in hierarchy_levels:
        print('  '.join(level))
    # Add a newline for clarity
    print()
    

initial_state = [["B"], ["C", "A"]]
goal_state = [["A", "B", "C"]]

on_table = OrderedDict()
on = OrderedDict()
clear = OrderedDict()
hand = None
current = []

# Populate initial state
for state in initial_state:
    # Top most (First) in list is clear
    clear[state[0]] = None
    # Bottom most (Last) in list is on table
    on_table[state[-1]] = None
    for i in range(len(state) - 1):
        # Blocks stacked
        on[state[i] + '*' + state[i + 1]] = None

# Print initial state
current = initial_state.copy()
hierarchy_levels = []
for sublist in current:
        for i, block in enumerate(sublist):
            # Ensure the hierarchy_levels list is long enough
            if len(hierarchy_levels) <= i:
                hierarchy_levels.append([])
            hierarchy_levels[i].append(block)
print("Initial state:")
for level in hierarchy_levels:
    print('  '.join(level))
print()

for goal in goal_state:
    execute_action(['CLEAR', goal[0]])
    for i in range(len(goal) - 2, -1, -1):
        execute_action(['ON', goal[i], goal[i + 1]])
    execute_action(['ONTABLE', goal[-1]])
    execute_action(['HANDEMPTY'])