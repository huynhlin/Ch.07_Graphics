'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''

import arcade
import random
palette = ["dd4444", "f48080", "2d676f", "194b4f"] # list of the colors i want to randomly select from
highlight = "ffdcdc" # kinda dislike this color so its on its own separate thing so i can minimize its appearance
base = "ede2c2"
arcade.open_window(700, 700, "Lindy Huynh")
arcade.set_background_color(arcade.color_from_hex_string(highlight))
counter = 0

arcade.start_render()
for x in range(2800): # background
    size = random.randint(20, 35)
    mixer = random.randint(1, 700)
    mixer2 = random.randint(1, 700)
    arcade.draw_circle_filled(mixer, mixer2, size, arcade.color_from_hex_string(random.choice(palette)))
    counter += 1
    if counter % 20 == 0:
        smixer = random.randint(1, 700)
        smixer2 = random.randint(1, 700)
        color = random.choice(palette)
        arcade.draw_rectangle_outline(smixer, smixer2, 50, 50, arcade.color_from_hex_string(color), 7)
        # crosses in boxes to make them look like crates
        left = smixer - 25; right = smixer + 25  # left and right coords for lines
        top = smixer2 + 25; bot = smixer2 - 25  # top and bottom coords for lines

        arcade.draw_line(left, top, right, bot, arcade.color_from_hex_string(color), 7)
        arcade.draw_line(right, top, left, bot, arcade.color_from_hex_string(color), 7)
arcade.draw_rectangle_filled(50, 50, 30, 30, arcade.color_from_hex_string(highlight))
arcade.draw_rectangle_filled(650, 650, 30, 30, arcade.color_from_hex_string(highlight))  # corner squares

# actual drawing now

# colors
# #d9d9d9 - base = 2
# #1f1f1f - outline/shadow = 1
# #4a4a4a - cloak = 3
# #757575 - nail = 4
# empty = 0

row1 = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
row2 = [0, 0, 0, 0, 1, 1, 2, 2, 2, 1]
row3 = [0, 0, 0, 1, 2, 2, 2, 2, 2, 1]
row4 = [0, 0, 0, 1, 2, 2, 2, 2, 1]
row5 = [0, 0, 1, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
row6 = [0, 0, 1, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 1, 1]
row7 = [0, 0, 1, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 1]
row8 = [0, 0, 1, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 1]
row9 = [0, 0, 1, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 1]
row10 = [0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1]
row11 = [0, 0, 0, 1, 2, 2, 2, 2, 2, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 2, 2, 1]
row12 = [0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1]
row13 = [0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1]
row14 = [0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1]
row15 = [0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
row16 = [0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1]
row17 = [0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1]
row18 = [0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1]
row19 = [0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 1]
row20 = [0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 1]
row21 = [0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 1]
row22 = [0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 1]
row23 = [0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 1]
row24 = [0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1]
row25 = [0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1]
row26 = [0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
row27 = [0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
row28 = [0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
row29 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
row30 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1]
row31 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 1, 1, 3, 3, 3, 3, 3, 1, 1, 1]
row32 = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1]
row33 = [0, 1, 3, 3, 3, 3, 1, 1, 1, 0, 0, 1, 1, 3, 3, 1, 3, 3, 1, 3, 3, 3, 1]
row34 = [0, 0, 1, 1, 1, 1, 3, 3, 3, 1, 1, 1, 3, 3, 1, 3, 1, 3, 1, 3, 3, 3, 1]
row35 = [0, 1, 3, 3, 3, 3, 3, 1, 1, 1, 3, 3, 3, 1, 3, 1, 3, 3, 1, 3, 3, 3, 3, 1]
row36 = [1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 1, 1, 3, 3, 1, 3, 1, 1, 1, 3, 1, 3, 1]
row37 = [0, 0, 1, 3, 3, 3, 3, 3, 1, 1, 1, 3, 3, 3, 1, 3, 3, 1, 1, 1, 3, 3, 1, 1]
row38 = [0, 0, 0, 1, 1, 1, 1, 1, 3, 3, 3, 3, 1, 1, 3, 3, 3, 1, 1, 1, 1, 3, 3, 1]
row39 = [0, 1, 1, 1, 1, 3, 3, 3, 3, 1, 1, 1, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1]
row40 = [0, 0, 1, 3, 3, 1, 1, 1, 1, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
row41 = [0, 0, 0, 1, 1, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 1]
row42 = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1]
row43 = [0, 0, 0, 0, 0, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 1, 1]
row44 = [0, 0, 0, 0, 0, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 1, 1]
row45 = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 1, 1]
row46 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 4, 1, 1, 4, 4, 1, 1]
row47 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 4, 4, 4, 4, 4, 1,
         1]
row48 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 4, 4, 4,
         4, 1, 1]
row49 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
         1, 4, 4, 1, 1]
row50 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 1, 1, 1]
row51 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]

rows = [row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11,
        row12, row13, row14, row15, row16, row17, row18, row19, row20, row21,
        row22, row23, row24, row25, row26, row27, row28, row29, row30, row31,
        row32, row33, row34, row35, row36, row37, row38, row39, row40, row41,
        row42, row43, row44, row45, row46, row47, row48, row49, row50, row51]

x_offset = 0
y_offset = 0

for row in rows:
    x_offset = 0
    for pixel in row:
        if pixel == 0:
            x_offset += 8
        if pixel == 1:
            arcade.draw_rectangle_filled(202 + x_offset, 552 - y_offset, 8, 8, arcade.color_from_hex_string("1f1f1f"))
            x_offset += 8
        if pixel == 2:
            arcade.draw_rectangle_filled(202 + x_offset, 552 - y_offset, 8, 8, arcade.color_from_hex_string("d9d9d9"))
            x_offset += 8
        if pixel == 3:
            arcade.draw_rectangle_filled(202 + x_offset, 552 - y_offset, 8, 8, arcade.color_from_hex_string("4a4a4a"))
            x_offset += 8
        if pixel == 4:
            arcade.draw_rectangle_filled(202 + x_offset, 552 - y_offset, 8, 8, arcade.color_from_hex_string("757575"))
            x_offset += 8
    y_offset += 8
# for row in list "rows"; for each number in the row, fills in a pixel which then increases offsets to move next dot
arcade.finish_render()

arcade.run()
