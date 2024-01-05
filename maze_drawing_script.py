import numpy as np
import math
import csv


def drawLine(canvas, x0, y0, x1, y1, value):
    """ Draw a simple line on the canvas, ensuring it stays within bounds. """
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x, y = x0, y0
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1

    if dx > dy:
        err = dx / 2.0
        while x != x1:
            if 0 <= y < canvas.shape[0] and 0 <= x < canvas.shape[1]:
                canvas[y, x] = value
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y1:
            if 0 <= y < canvas.shape[0] and 0 <= x < canvas.shape[1]:
                canvas[y, x] = value
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy

    # Ensure final point is plotted if within bounds
    if 0 <= y < canvas.shape[0] and 0 <= x < canvas.shape[1]:
        canvas[y, x] = value


def drawThickLine(canvas, x0, y0, x1, y1, value, thickness):
    """ Draw a thick line on the canvas. """
    dx = x1 - x0
    dy = y1 - y0
    normalX, normalY = -dy, dx
    length = math.sqrt(normalX ** 2 + normalY ** 2)
    normalX, normalY = normalX / length, normalY / length

    for i in range(-thickness // 2, thickness // 2 + 1):
        offsetX = int(i * normalX)
        offsetY = int(i * normalY)
        drawLine(canvas, x0 + offsetX, y0 + offsetY, x1 + offsetX, y1 + offsetY, value)

def draw_filled_circle(canvas, center_x, center_y, radius):
    for y in range(center_y - radius, center_y + radius + 1):
        for x in range(center_x - radius, center_x + radius + 1):
            if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2:
                if 0 <= x < canvas.shape[1] and 0 <= y < canvas.shape[0]:
                    canvas[y, x] = 1


"""def draw_maze(canvas):
    #Draw the maze on the canvas. 
    drawThickLine(canvas, 5, 5, 5, 205, 1, 10)  # Left border
    drawThickLine(canvas, 5, 5, 315, 5, 1, 10)  # Top border
    drawThickLine(canvas, 5, 235, 315, 235, 1, 10)  # Bottom border
    drawThickLine(canvas, 315, 5, 315, 235, 1, 10)  # Right border

    # Additional internal walls or obstacles
    drawThickLine(canvas, 50, 50, 150, 50, 1, 10)  # Example horizontal wall
    drawThickLine(canvas, 200, 100, 200, 200, 1, 10)  # Example vertical wall
    drawThickLine(canvas, 270, 10, 270, 50, 1, 10)  # Vertical
    drawThickLine(canvas, 50, 100, 50, 200, 1, 10)  # Vertical
    drawThickLine(canvas, 50, 150, 200, 150, 1, 10)  # Horizontal
    drawThickLine(canvas, 50, 200, 100, 200, 1, 10)  # Horizontal
    drawThickLine(canvas, 100, 200, 100, 230, 1, 10)"""
def draw_maze(canvas):
    drawThickLine(canvas, 80, 100, 80, 140, 1, 10)
    drawThickLine(canvas, 60, 120, 100, 120, 1, 10)

    drawThickLine(canvas, 140, 120, 180, 120, 1, 20)

    # (240, 120)
    draw_filled_circle(canvas, 240, 120, 20)

def write_to_csv(canvas, filename):
    """ Write the canvas array to a CSV file in the specified format. """
    with open(filename, 'w', newline='') as file:
        for row in canvas:
            formatted_row = '{' + ','.join(map(str, row)) + '}'
            file.write(formatted_row + ',\n')


# Create a 240x320 canvas
canvas = np.zeros((240, 320), dtype=int)

# Draw the maze
draw_maze(canvas)

# Write the canvas to a CSV file
csv_file = 'maze_canvas.txt'
write_to_csv(canvas, csv_file)
