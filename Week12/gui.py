import tkinter as tk
import number_entry as numy


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = tk.Frame(root)
    frm_main.master.title("Rectangle Area")
    frm_main.pack(padx=8, pady=6, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()

def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.
    
    Parameter
        frm_main: the main window
    Return: nothing
    """
    # Create a label that displays "width:"
    lbl_width = tk.Label(frm_main, text="width:")
    lbl_height = tk.Label(frm_main, text='height:')

    # Create a integer entry box where the user will enter her width.
    ent_width = numy.IntEntry(frm_main, 1, 1000000, width=5)
    ent_height = numy.IntEntry(frm_main, 1, 1000000, width=5)

    # Create a label that displays "Rates:"
    lbl_area = tk.Label(frm_main, text="Area:")

    # Create labels that will display the results.
    lbl_area_value = tk.Label(frm_main, width=4)

    # Create the Clear button.
    btn_clear = tk.Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_width.grid(  row=0, column=0, padx=3, pady=3)
    ent_width.grid(  row=0, column=1, padx=3, pady=3)
    lbl_height.grid(row=0, column=2, padx=3, pady=3)
    ent_height.grid(row=0, column=3, padx=3, pady=3)
    lbl_area.grid(row=0, column=4, padx=(30,3), pady=3)
    lbl_area_value.grid( row=0, column=5, padx=3, pady=3)
    btn_clear.grid(row=1, column=0, padx=3, pady=3, columnspan=5, sticky="W")


    # This function will be called each time the user releases a key.
    def calc(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            # Get the user's width.
            width = ent_width.get()
            height = ent_height.get()

            # Compute the user's maximum heart rate.
            area_value = height * width

            # Compute the user's slowest and
            # fastest beneficial heart rates.
            

            # Display the slowest and fastest benficial
            # heart rates for the user to see.
            lbl_area_value.config(text=f"{area_value:.0f}")

        except ValueError:
            # When the user deletes all the digits in the width
            # entry box, clear the slowest and fastest labels.
            lbl_area_value.config(text="")



    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        ent_width.delete(0, tk.END)
        ent_height.delete(0, tk.END)
        lbl_area_value.config(text="")
        ent_width.focus()


    # Bind the calc function to the width entry box so
    # that the calc function will be called when the
    # user changes the text in the entry box.
    ent_width.bind("<KeyRelease>", calc)
    ent_height.bind("<KeyRelease>", calc)

    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the width entry box.
    ent_width.focus()


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
