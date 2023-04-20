"""A Python program that uses the Tkinter library
to draws a semi-realistic 
outdoor scene in a computer window. 
The scene must be outdoor and include part of the sky.
The sky must have clouds.
The scene must include repetitive objects,
such as blades of grass, trees, leaves on a tree,
birds, flowers, insects, fish, pickets in a fence,
dashed lines on a road, buildings, bales of hay, snowmen,
snowflakes, or icicles.
"""


# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500
    interval = 50
    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)
    
    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    """Call the draw pine tree function to draw
     pine trees at the different positions"""
    draw_pine_tree(canvas, 100, 120, 120,)
    draw_pine_tree(canvas, 200, 120, 120)
    draw_pine_tree(canvas, 750, 120, 120)
    for x in range (50, 340, 100):
        draw_pine_tree(canvas, x, 80, 120)
    draw_house(canvas, 550, 100, 150)
    #draw_grid(canvas, scene_width, scene_height, interval)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
"""draw the Sky and all object in the sky"""
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height - 300,
                   scene_width, scene_height, width=0, fill="sky blue")
    draw_oval(canvas, 810, 510, 610, 350, width=1,
              outline="yellow", fill="yellow")
    draw_oval(canvas, 50, 352, 200, 375, width=1,
              outline="mistyRose1", fill="mistyRose1")
    draw_oval(canvas, 90, 390, 210, 365, width=1,
              outline="mistyRose1", fill="mistyRose1")
    draw_oval(canvas, 120, 410, 235, 383, width=1,
              outline="mistyRose1", fill="mistyRose1")
    draw_oval(canvas, 400, 450, 550, 383, width=1,
              outline="mistyRose1", fill="mistyRose1")
    draw_oval(canvas, 380, 410, 500, 460, width=1,
              outline="mistyRose1", fill="mistyRose1")
    for y in range (350, 550, 30):
        draw_oval(canvas, y, 80, 120, 400)

"""Draw the ground and all the objects on the ground."""
def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0,
                   scene_width, scene_height - 300, width=0, fill="green3")

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
       canvas: The canvas where this function
           will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
           this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
           this function will draw.
    Return: nothing
    """
    #Draw the trunk of the tree
    trunk_width = height/6
    trunk_height = height/4
    trunk_left = center_x - trunk_width/2
    trunk_bottom = bottom
    trunk_right = center_x + trunk_width/2
    trunk_top = bottom + trunk_height
    #Draw rectangle
    draw_rectangle(canvas, trunk_left, trunk_bottom, 
                   trunk_right, trunk_top, width=1,
                   outline="tan4", fill="tan4")

    #Draw the skirt of the tree
    skirt_left = center_x - 30
    skirt_bottom = trunk_top
    skirt_center = center_x
    skirt_top = 250
    skirt_right = center_x + 30
    draw_polygon(canvas,skirt_left, skirt_bottom, skirt_center, 
                 skirt_top, skirt_right, skirt_bottom, width=1,
                 outline="forestgreen", fill="forestgreen")


#Draw a house
def draw_house(canvas, house_center, house_bottom, house_height):
    #Draw the rectangular base of the house
    base_left = house_center - 150
    base_bottom = house_bottom  # =100
    base_right = house_center + 150
    base_top = house_bottom + 100
    draw_rectangle(canvas, base_left, base_bottom,
                   base_right, base_top, width=2, outline="maroon4", fill="maroon4")

    #Draw another rectangle to form a part of the house roof
    new_base_left = house_center - 150
    new_base_bottom = 200
    new_base_right = house_center + 150
    new_base_top = 250
    draw_rectangle(canvas, new_base_left, new_base_bottom, new_base_right, 
                   new_base_top, width=3, outline="gray51", fill="gray51")

    #Draw the door of the house
    door_left = house_center - 20
    door_right = house_center + 20
    door_top = house_bottom + 50
    door_bottom = house_bottom

    # Draw the rectangle
    draw_rectangle(canvas,
                   door_left, door_top, door_right, door_bottom,
                   outline="gray5", width=2, fill="tan3")

    #draw the windows
    #draw the first window
    first_window_left = house_center - 120
    first_window_right = house_center - 80
    first_window_top = house_bottom + 80
    first_window_bottom = house_bottom + 50
    # Draw the rectangle
    draw_rectangle(canvas,
                   first_window_left, first_window_top, first_window_right, 
                   first_window_bottom, outline="gray5", width=2, fill="linen")

    #draw the second window
    second_window_left = house_center + 80
    second_window_right = house_center + 120
    second_window_top = house_bottom + 80
    second_window_bottom = house_bottom + 50
    # Draw the rectangle
    draw_rectangle(canvas,
                   second_window_left, second_window_top, second_window_right, 
                   second_window_bottom, outline="gray5", width=2, fill="linen")
    #Draw the crowns of the roof
    #draw the left crown of the house roof
    left_crown_left = house_center - 200
    left_crown_right = house_center - 150
    left_crown_top = house_bottom + 150
    left_crown_bottom = house_bottom + 100
    draw_polygon(canvas, left_crown_left, left_crown_bottom, left_crown_right, 
                left_crown_bottom, left_crown_right, left_crown_top,
                width=3, outline="gray51", fill="gray51")

    #draw the right crown of the house roof
    right_crown_left = house_center + 150
    right_crown_right = house_center + 200
    right_crown_top = house_bottom + 150
    right_crown_bottom = house_bottom + 100
    draw_polygon(canvas, right_crown_left, right_crown_bottom, right_crown_right, 
                right_crown_bottom, right_crown_left, right_crown_top, width=3, 
                outline="gray51", fill="gray51")
"""
#define the grid function to draw the grid for accurate measurement
def draw_grid(canvas, width, height, interval):
    #draw a vertical line at every interval 
    label_y = 15
    for x in range (interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")

    #draw a horinzontal line at every interval
    label_x = 15
    for y in range (interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}")
"""
# Call the main function so that
# this program will start executing.
main()
