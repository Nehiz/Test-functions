

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500
    
    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_pine_tree(canvas, 100, 100, 200)
    draw_house(canvas, 550, 100, 200)
    #draw_house(canvas, 350, 100)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky (canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue" )
        
    draw_oval (canvas, 800, 500, 250, 300, fill="floralWhite")
#draw_oval(canvas, x0, y0, x1, y1, width=1, outline="black", fill="")

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="green1")

    # Draw a pine tree.
    tree_center_x = 200
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,
                   tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 300
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,
                   tree_bottom, tree_height)


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
    #Draw the trunk of the pine tree
    trunk_width = height / 8
    trunk_height = height / 5
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas, 
            trunk_left, trunk_top, trunk_right, bottom, 
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
                 skirt_right, trunk_top,
                 skirt_left, trunk_top,
                 outline="gray20", width=1, fill="green4")

#Draw a house
def draw_house(canvas, house_center, house_bottom, house_height):
    #Draw the rectangular base of the house
    base_width = house_height + 50
    base_height = house_height - 50
    base_left = house_center - 150
    base_bottom = house_bottom #=100
    base_right = house_center + 150
    base_top = house_bottom + 100
    draw_rectangle(canvas, base_left, base_bottom,
                   base_right, base_top, fill="maroon4")
    
     #Draw another rectangular base to form a part of the house roof
    new_base_left = house_center - 150
    new_base_bottom = 200
    new_base_right = house_center + 150
    new_base_top = 250
    draw_rectangle(canvas, new_base_left, new_base_bottom, new_base_right, new_base_top,
                    width=3, outline= "black", fill="pink2")

    #Draw the door of the house
    door_width = 30
    door_height = 35
    door_left = house_center - 25
    door_right = house_center + 25
    door_top = house_bottom + 50
    door_bottom = house_bottom

    # Draw the rectangle
    draw_rectangle(canvas,
                   door_left, door_top, door_right, door_bottom,
                   outline="gray20", width=1, fill="tan3")

    #draw the windows
    #draw the first window
    first_window_left = house_center - 120
    first_window_right = house_center - 80
    first_window_top = house_bottom + 80
    first_window_bottom = house_bottom + 50
    # Draw the rectangle
    draw_rectangle(canvas,
                   first_window_left, first_window_top, first_window_right, first_window_bottom,
                   outline="gray20", width=1, fill="tan3")

    #draw the second window
    second_window_left = house_center + 80
    second_window_right = house_center + 120
    second_window_top = house_bottom + 80
    second_window_bottom = house_bottom + 50
    # Draw the rectangle
    draw_rectangle(canvas,
                   second_window_left, second_window_top, second_window_right, second_window_bottom,
                   outline="gray20", width=1, fill="tan3")


    #draw the left crown of the house roof
    left_crown__width = 50
    left_crown_height = 50
    left_crown_left = house_center - 200
    left_crown_right = house_center -150
    left_crown_top = house_bottom + 150
    left_crown_bottom = house_bottom + 100
    draw_polygon(canvas, left_crown_left, left_crown_bottom, left_crown_right, left_crown_bottom, left_crown_right, left_crown_top,
                 width=3, outline="black", fill="pink2")

    #draw the right crown of the house roof
    right_crown__width = 50
    right_crown_height = 50
    right_crown_left = house_center + 150
    right_crown_right = house_center + 200
    right_crown_top = house_bottom + 150
    right_crown_bottom = house_bottom + 100
    draw_polygon(canvas, right_crown_left, right_crown_bottom, right_crown_right, right_crown_bottom, right_crown_left, right_crown_top,
                 width=3, outline="black", fill="pink2")
    #draw_polygon(canvas, left_crown_left, left_crown_bottom, left_crown_right, left_crown_bottom, left_crown_right, left_crown_top,
                #width=3, outline="black", fill="")
   #draw_polygon(canvas,skirt_left, skirt_bottom, skirt_center, skirt_top, skirt_right, skirt_bottom, fill="forestgreen")
"""
    draw_line(canvas, 600, 500, 460, 200, width=1, fill="yellow4")

     #Draw another line     
    draw_line(canvas, 450, 700, 800, 200, width=1, fill="yellow4")
"""


# Call the main function so that
# this program will start executing.
main()
