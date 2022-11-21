import arcade
import random
palette = ["dd4444", "f48080", "2d676f", "194b4f"] # list of the colors i want to randomly select from
highlight = "ffdcdc" # kinda dislike this color so its on its own separate thing so i can minimize its appearance
base = "ede2c2"
arcade.open_window(600,600, "Lindy Huynh")
arcade.set_background_color(arcade.color.WHITE)
counter = 0
arcade.start_render()

smixer = random.randint(1, 600)
smixer2 = random.randint(1, 600)
fillint = smixer
fillint2 = smixer2
color = random.choice(palette)
arcade.draw_rectangle_outline(fillint, fillint2, 50, 50, arcade.color_from_hex_string(color), 7)
# crosses in boxes to make them look like crates
left = fillint - 25
top = fillint2 + 25
bot = fillint2 - 25
right = fillint + 25
arcade.draw_line(left, top, right, bot, arcade.color_from_hex_string(color), 7)
arcade.draw_line(right, top, left, bot, arcade.color_from_hex_string(color), 7)
arcade.draw_text(smixer, 200, 500, arcade.color.BLACK, 30)
arcade.draw_text(smixer2, 200, 450, arcade.color.BLACK, 30)
arcade.draw_text(fillint, 200, 400, arcade.color.BLACK, 30)
arcade.draw_text(fillint2, 200, 350, arcade.color.BLACK, 30)
arcade.draw_text(top, 200, 300, arcade.color.BLACK, 30)
arcade.draw_text(bot, 200, 250, arcade.color.BLACK, 30)
arcade.draw_text(left, 200, 200, arcade.color.BLACK, 30)
arcade.draw_text(right, 200, 150, arcade.color.BLACK, 30)

arcade.finish_render()

arcade.run()
