'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red: #BF0A30 and blue: #002868
Title the window, "The Stars and Stripes"
You can use a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
CHALLENGE: Can you make the entire flag parametrically? This means if I change the hoist to 520px the flag will resize accordingly.
'''
import arcade
arcade.open_window(494, 260, "Stars and Stripes"), arcade.set_background_color(arcade.color.WHITE), arcade.start_render()

for stripe in range(0, 260, 40):
    arcade.draw_lrtb_rectangle_filled(0, 494, 20+stripe, 0+stripe, (191, 10, 48))
    arcade.draw_lrtb_rectangle_filled(0, 197.6, 260, 120, (0, 40, 104))
arcade.draw_rectangle_filled(0, 195, 400, 130, arcade.color_from_hex_string("#002868"))

for star in range(0,5,1):
    for horz in range (0,17,16):
        for vert in range(226,110, -28):
            for s2_off in range(12,179,32):
                if ((horz)+(s2_off)) > 180:
                    break
                elif ((vert)-(horz)) < 110:
                    break
                else:
                    arcade.draw_text("*", ((s2_off)+(horz)), ((vert)-((horz)-0.3*(horz))), arcade.color.WHITE, 20)
# took a bit of inspiration from alumnis :)
arcade.finish_render(), arcade.run()