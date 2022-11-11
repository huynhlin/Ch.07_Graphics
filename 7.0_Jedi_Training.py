# Sign your name: Lindy Huynh

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
arcade.open_window(500, 400, "chapter 7 test image")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()
x_offset = 0
y_offset = 0
for x in range(25): # GRID LINES
    arcade.draw_line(20 + x_offset, 0, 20 + x_offset, 500, arcade.color.BLACK, 1)
    x_offset += 20
    arcade.draw_line(0, 20 + y_offset, 500, 20 + y_offset, arcade.color.BLACK, 1)
    y_offset += 20
arcade.draw_point(460, 10, arcade.color.RED, 5) # red dot in bot right
arcade.draw_line(80, 20, 120, 60, arcade.color.BLUE, 1) # blue line in bot left
arcade.draw_rectangle_filled(50, 370, 60, 20, arcade.color.PHLOX) # rectangle top left
arcade.draw_circle_filled(250, 200, 40, arcade.color.WISTERIA) # center circle
arcade.draw_rectangle_filled(200, 260, 40, 20, arcade.color.BLUSH, 135) # tilted rectangle mid
arcade.draw_ellipse_filled(100, 100, 120, 40, arcade.color.AMBER) # amber ellipse bot left
arcade.draw_text("I love you. I know.", 20, 160, arcade.color.BRICK_RED, 20) # text next to circle
arcade.draw_arc_filled(400, 320, 120, 120, arcade.color.YELLOW, 0, 300, 30) # pac man - angles are very hard holyy that took a while
arcade.finish_render()
arcade.run()
