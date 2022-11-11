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
arcade.open_window(500,500, "Stars and Stripes")
arcade.start_render()

arcade.draw_rectangle_filled(250,250,400,260,arcade.color.RED)
# blue rectangle under stars
ex = 15
why = 100
counter = 0
for x in range(50):
    arcade.draw_text(" * ", 39 + ex, 250 + why, arcade.color.WHITE, 20)
    ex += 15
    counter += 1
    if counter == 10:
        counter = 0
        why -= 15
        ex = 15
# white stripes
arcade.finish_render()
arcade.run()