import turtle

tim = turtle.Turtle()

# ----------- File Handling -----------
def read_file(file_path : str) -> list:
    file = open(file_path, "r")
    return file.read().splitlines()

# def read_line(line : str) -> list:
#     return line.split()

def read_lines(lines : list) -> list:
    valid_lines = []
    for line in lines:
        split_line = line.split()
        if len(split_line) == 0:
            continue
        valid_lines.append(split_line)
    return valid_lines

# takes a command and executes the functions
# returns a line the progam should jump to
def interpret_command(line : list):
    global all_counters, all_commands
    read_line = line[:]

    if line[0] in all_commands:
        command = all_commands[read_line[0]]
        # print(read_line[1])

        # if not read_line[1].lstrip("-").isdigit():
        #     read_line[1] = all_counters[line[1]]
        return command(*read_line[1:])

    elif line[0] == "#":
        return

# ----------- Commands -----------
def go(*args):
    dist = name_to_int(args[0]) # distance the turtle travels
    tim.forward(dist)

def turn(*args):
    deg = name_to_int(args[0]) # degrees the turtle turns in given direction
    direction = args[1]
    if direction == "left":
        tim.left(deg)
    elif direction == "right":
        tim.right(deg)

def square(*args):
    length = name_to_int(args[0])
    for i in range(4):
        tim.forward(length)
        tim.left(90)

def jump_to(*args) -> int: 
    val = name_to_int(args[0])
    return val - 1 # line numbers in text editors typically start at 1

# creates essentially a variable for the language to read
def counter(*args): 
    global all_counters

    start_val = name_to_int(args[0])
    name = args[1]

    all_counters[name] = start_val

# increases a counter by a set value
def count(*args):
    global all_counters

    increase_amount = name_to_int(args[0])
    counter_name = args[1]

    all_counters[counter_name] += increase_amount

def conditional(*args):
    val1 = name_to_int(args[0])
    val2 = name_to_int(args[2])
    sign = args[1] # sign for comapring ie >, <, <=, >=
    next_line = args[3:]

    do_line = eval(str(val1) + sign + str(val2))
    if do_line:
        return interpret_command(next_line)

# stores all counters
all_counters = {}

all_commands = {
    "go": go,
    "turn": turn,
    "jump": jump_to,
    "counter": counter,
    "count": count,
    "if": conditional,
    "square": square,
}

# ----------- Other Functions -----------

def name_to_int(name) -> int:
    if name.lstrip("-").isdigit():
        return int(name)
    if name in all_counters:
        return all_counters[name]

# ----------- Main Function -----------
def run(path : str):
    all_lines = read_file(path)
    all_lines = read_lines(all_lines)

    tim.reset()

    running = True

    line_num = 0
    total_lines = 0
    
    while running:
        reading = all_lines[line_num]

        jump_to = interpret_command(reading)

        if reading[0] == "end":
            running = False
        
        if jump_to != None:
            line_num = jump_to
        else: 
            line_num += 1 

        total_lines += 1 
        # print(total_lines)
        if total_lines > 1000:
            break  
 
    turtle.mainloop()

#run(file_name)