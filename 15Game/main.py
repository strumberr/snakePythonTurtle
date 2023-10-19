import turtle
import random

GRID_SIZE = 4
CELL_SIZE = 50
EMPTY_CELL = -1

matrix = [[(GRID_SIZE * i + j) + 1 for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]
matrix[-1][-1] = EMPTY_CELL


def color_cell(row, col, color):
    turtle.hideturtle()
    turtle.penup()
    start_x = -CELL_SIZE * GRID_SIZE / 2 + col * CELL_SIZE
    start_y = CELL_SIZE * GRID_SIZE / 2 - (row) * CELL_SIZE
    turtle.goto(start_x, start_y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(CELL_SIZE)
        turtle.right(90)
    turtle.end_fill()
    turtle.update()


def color_rounded_cell(row, col, color):
    turtle.hideturtle()
    turtle.penup()

    start_x = -CELL_SIZE * GRID_SIZE / 2 + col * CELL_SIZE
    start_y = CELL_SIZE * GRID_SIZE / 2 - (row + 1) * CELL_SIZE

    turtle.goto(start_x + CORNER_RADIUS, start_y)
    turtle.pendown()
    
    turtle.fillcolor("white")
    turtle.begin_fill()

    
    for _ in range(4):
        turtle.forward(CELL_SIZE - 2 * CORNER_RADIUS)
        turtle.circle(CORNER_RADIUS, 90)


    for _ in range(7):
        turtle.penup()
        turtle.goto(start_x + CORNER_RADIUS, start_y + CELL_SIZE)
        turtle.pendown()
        turtle.forward(CELL_SIZE - 2 * CORNER_RADIUS)

        start_y -= CELL_SIZE/6


    start_y = CELL_SIZE * GRID_SIZE / 2 - (row + 1) * CELL_SIZE

    for _ in range(7):
        turtle.penup()
        turtle.goto(start_x, start_y - CORNER_RADIUS + 10)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(CELL_SIZE - 2 * CORNER_RADIUS)
        turtle.right(90)
        
        start_x += CELL_SIZE / 6


    start_x = -CELL_SIZE * GRID_SIZE / 2 + col * CELL_SIZE


    turtle.end_fill()
    turtle.update()
    

CORNER_RADIUS = 5

def draw_rounded_square(x, y, size):
    turtle.penup()
    turtle.goto(x + CORNER_RADIUS, y)
    turtle.pendown()
    turtle.width(2)
    
    for _ in range(4):
        turtle.forward(size - 2 * CORNER_RADIUS)
        turtle.circle(CORNER_RADIUS, 90)


def draw_grid():
    turtle.clear()
    turtle.speed(0)
    turtle.hideturtle()
    turtle.tracer(0, 0)
    
    start_x = -CELL_SIZE * GRID_SIZE / 2
    start_y = -CELL_SIZE * GRID_SIZE / 2
    
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = start_x + col * CELL_SIZE
            y = start_y + row * CELL_SIZE
            
            draw_rounded_square(x, y, CELL_SIZE)

            if matrix[row][col] != EMPTY_CELL:

                draw_number(row, col, matrix[row][col])
            else:
                color_rounded_cell(row, col, "light blue")


                
    turtle.update()

def draw_number(row, col, num):

    turtle.hideturtle()
    turtle.penup()
    x = -CELL_SIZE * GRID_SIZE / 2 + col * CELL_SIZE + (CELL_SIZE/2)
    y = CELL_SIZE * GRID_SIZE / 2 - (row) * CELL_SIZE - (CELL_SIZE/2)
    turtle.goto(x, y - 13)
    turtle.write(num, align="center", font=("Bagel Fat One", 80, "normal"))
    turtle.update()


def get_empty_cell():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if matrix[row][col] == EMPTY_CELL:
                return row, col


def is_adjacent(row1, col1, row2, col2):
    
    return (row1 == row2 and abs(col1 - col2) == 1) or (col1 == col2 and abs(row1 - row2) == 1)

def is_adjacent(row1, col1, row2, col2):
    
    return (row1 == row2 and abs(col1 - col2) == 1) or (col1 == col2 and abs(row1 - row2) == 1)

    
def click_handler(x, y):
    col = int((x + CELL_SIZE * GRID_SIZE / 2) // CELL_SIZE)
    row = int((-y + CELL_SIZE * GRID_SIZE / 2) // CELL_SIZE)
    empty_row, empty_col = get_empty_cell()

    print(is_adjacent(row, col, empty_row, empty_col))

    if is_adjacent(row, col, empty_row, empty_col):
        matrix[row][col], matrix[empty_row][empty_col] = matrix[empty_row][empty_col], matrix[row][col]
        print(matrix)
        draw_grid()

    
def get_empty_cell():
    for row in range(GRID_SIZE):

        for col in range(GRID_SIZE):
            if matrix[row][col] == EMPTY_CELL:

                return row, col
            
def cells_around(direction):
    cells = []
    row, col = get_empty_cell()
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < GRID_SIZE and 0 <= new_col < GRID_SIZE:
                cells.append((new_row, new_col))
    
    print("empty cell: ", row, col)
    print("cells around: ", cells)


    if direction == "up":
        for el in cells:
            if el[0] - 1 == row:
                print("can move up: ", (el[1] - 1), row)
                matrix[el[0]][el[1]], matrix[el[0] - 1][el[1]] = matrix[el[0] - 1][el[1]], matrix[el[0]][el[1]]
        draw_grid()
    elif direction == "down":
        for el in cells:
            if el[0] + 1 == row:
                print("can move down: ", (el[1] + 1), row)
                matrix[el[0]][el[1]], matrix[el[0] + 1][el[1]] = matrix[el[0] + 1][el[1]], matrix[el[0]][el[1]]
        draw_grid()
    elif direction == "left":
        for el in cells:
            if el[1] - 1 == col:
                print("can move left: ", (el[1] - 1), col)
                matrix[el[0]][el[1]], matrix[el[0]][el[1] - 1] = matrix[el[0]][el[1] - 1], matrix[el[0]][el[1]]
        draw_grid()
    elif direction == "right":
        for el in cells:
            if el[1] + 1 == col:
                print("can move right: ", (el[1] + 1), col)
                matrix[el[0]][el[1]], matrix[el[0]][el[1] + 1] = matrix[el[0]][el[1] + 1], matrix[el[0]][el[1]]
        draw_grid()

    return cells


def shuffle_board():
    for _ in range(1000):
        empty_row, empty_col = get_empty_cell()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)

        # print(matrix)

        print(directions)

        for dr, dc in directions:
            new_row, new_col = empty_row + dr, empty_col + dc
            if 0 <= new_row < GRID_SIZE and 0 <= new_col < GRID_SIZE:
                matrix[new_row][new_col], matrix[empty_row][empty_col] = matrix[empty_row][empty_col], matrix[new_row][new_col]
                break

    draw_grid()


screen = turtle.Screen()
screen.tracer(0)
screen.setworldcoordinates(-CELL_SIZE*GRID_SIZE/2, -CELL_SIZE*GRID_SIZE/2, CELL_SIZE*GRID_SIZE/2, CELL_SIZE*GRID_SIZE/2)

draw_grid()
shuffle_board()

turtle.onscreenclick(click_handler)

turtle.onkey(lambda: cells_around("up"), "Up")
turtle.onkey(lambda: cells_around("down"), "Down")
turtle.onkey(lambda: cells_around("left"), "Left")
turtle.onkey(lambda: cells_around("right"), "Right")

turtle.listen()

turtle.mainloop()