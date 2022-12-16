import tkinter as tk
import random


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_sky(canvas, 0, 0, width-1, height-1)
    draw_clouds(canvas, 100, 100, 150, 50, 3)
    draw_scene(canvas, 0, 0, width-1, height-1)
    draw_grass_blade(canvas, width, 0, height, 60)
    draw_picket(canvas, 0, height, 15, width)
    draw_grass_blade(canvas, width, 0, height, 60, color='#90ee90', height_max=46, height_min=15)
    draw_sun(canvas, 570, 115, 150)
    

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    tree_center = scene_left + 505
    tree_top = scene_top + 100
    tree_height = 360
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.


def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")


# Call the main function so that
# this program will start executing.

def draw_sky(canvas, x_top, y_left, x_bottom, y_right, color='#99CCFF'):
    canvas.create_rectangle(x_top, y_left, x_bottom, y_right, fill=color)

def draw_clouds(canvas, x_top, y_left, cloud_width, cloud_height, number_clouds, color='white'):
       
    x_bottom = x_top + cloud_width
    y_right = y_left + cloud_height
    for i in range(number_clouds):
        x_bottom += i * 100 
        x_top += i* 100
        if i // 2 == 0:
            y_left += i * 50
            y_right += i * 50
        else:
            y_left += i * -50
            y_right += i * -50

        for i in range(2):
            if i != 0:
                resize_cloud_x = i * 1.1
                resize_cloud_y = i * 1
                move_cloud_y = i * 20
                move_cloud_x = i * 20 + 20
            else:
                resize_cloud_x = 1
                resize_cloud_y = 1
                move_cloud_y = 0
                move_cloud_x = 0
            canvas.create_oval(x_top + move_cloud_x, y_left + move_cloud_y, x_bottom * resize_cloud_x, y_right * resize_cloud_y, fill=color, width=0)



# def draw_house(canvas, house_left, house_bottom):

# def draw_bird(canvas, bird_center, bird_top):

# def draw_pebble(canvas, pebble_left, pebble_top, pebble_radius):

def draw_picket(canvas, picket_left, picket_bottom, number_of_pickets, width):
    picket_width = width / number_of_pickets - 20
    picket_top = picket_bottom - 150
    
    for i in range(number_of_pickets):
        picket_right = picket_left + picket_width
        canvas.create_rectangle(picket_left, picket_bottom, picket_right, picket_top, fill='white', width=False)
        canvas.create_polygon(picket_left - 1, picket_top, picket_right, picket_top, picket_width / 2 + picket_left, picket_top - 30, fill='white', width=False)
        picket_left += width / number_of_pickets

def draw_grass_blade(canvas, drawing_width, blade_start_x, blade_start_y, number_of_blades, blade_height=-1, color='green', height_max=101, height_min=30):
    if blade_height < 0:
        blade_height = lambda x: x - random.randrange(height_min, height_max, 15)
    else:
        pass
    blade_width = drawing_width / number_of_blades
    
    for i in range(number_of_blades):
        canvas.create_rectangle(blade_start_x, blade_start_y, blade_start_x + blade_width, blade_height(blade_start_y) - random.randrange(1, 16, 4), fill=color, width=False)
        blade_start_x += blade_width
        # print(blade_start_y + blade_height(blade_start_))
    # canvas.create_rectangle(0, 500, drawing_width, 400, fill='green')

def draw_sun(canvas, x_start, y_start, width):
    x_end = x_start + width
    y_end = y_start + width
    lense1_start = x_start + 1/4 * width
    lense1_start_y = y_start + 1/3 * width
    glasses_size = 25
    lense2_start = x_end - 1/4 * width
    lense2_end = lense2_start - glasses_size
    
    # arc_end = y_start + 1/3 * width
    canvas.create_oval(x_start, y_start, x_end, y_end, fill='#ffff77', width=False)
    canvas.create_oval(lense1_start, lense1_start_y, lense1_start + glasses_size, lense1_start_y + glasses_size * 1.3,fill='black')
    canvas.create_oval(lense2_start, lense1_start_y, lense2_end, lense1_start_y + glasses_size * 1.3,fill='black')
    canvas.create_arc(lense1_start - glasses_size, lense1_start_y + 50, lense2_start, lense1_start_y + 50, fill='black', start=25)

main()

