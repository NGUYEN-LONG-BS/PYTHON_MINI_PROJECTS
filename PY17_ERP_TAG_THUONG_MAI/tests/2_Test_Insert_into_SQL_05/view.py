# view.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class CRUDTreeviewView:
    def __init__(self, master):
        self.master = master
        self.master.title("CRUD Treeview Example")
        # =======================================================================================================================
        # Get the screen height and width
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        # Set the window height to 4/5 of the screen height
        window_height = int(4 * screen_height / 5)
        # Set the window width (you can adjust as needed)
        window_width = window_height // 9 * 16
        # Calculate the position to center the window
        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)
        # Set the window geometry (centered window)
        self.master.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        
        # =======================================================================================================================
        # Create a canvas and a vertical scrollbar
        self.canvas = tk.Canvas(self.master, width=window_width)
        self.canvas.pack(side="left", fill="both", expand=True)
        
        self.v_scrollbar_of_frame_inside_canvas = tk.Scrollbar(self.master, orient="vertical", command=self.canvas.yview, bg="lightyellow")
        self.v_scrollbar_of_frame_inside_canvas.pack(side="right", fill="y")
        # Configure the canvas to work with the scrollbar
        self.canvas.configure(yscrollcommand=self.v_scrollbar_of_frame_inside_canvas.set)

        # =======================================================================================================================
        # Create a frame to hold the widgets (this frame will be inside the canvas)
        frame_inside_canvas = tk.Frame(self.canvas, bd=2, relief="solid")
        frame_inside_canvas.pack(fill="x", side="top", padx=10, pady=10)

        # Create a window on the canvas to add the frame
        self.canvas_window = self.canvas.create_window(0, 0, window=frame_inside_canvas, anchor="nw")

        # =======================================================================================================================
        # Create the frame to hold the entry fields
        self.header_frame = tk.Frame(frame_inside_canvas, bd=2, relief="solid")
        self.header_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # =======================================================================================================================
        # Create the frame to hold the entry fields
        self.entries_frame = tk.Frame(frame_inside_canvas, bd=2, relief="solid")
        self.entries_frame.pack(fill="both", expand=True, padx=10, pady=10)
        # Create 10 Entry fields for input
        self.f_add_entries_to_entries_frame()
        
        # =======================================================================================================================
        # Create the frame to hold the Treeview and scrollbar
        self.treeview_frame = tk.Frame(frame_inside_canvas, bd=2, relief="solid", bg="lightyellow")
        self.treeview_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.f_add_elements_to_treeview_frame()
        
        # Bind mouse wheel events to both treeview and canvas
        self.treeview_frame.bind("<Enter>", self.f_enable_treeview_scroll)
        self.treeview_frame.bind("<Leave>", self.f_enable_canvas_scroll)

        # =======================================================================================================================
        # Create a frame for the top-right button (Refresh Button)
        self.top_right_frame = tk.Frame(self.header_frame, bd=2, relief="solid")
        self.top_right_frame.grid(row=0, column=10, padx=10, pady=10, sticky="ne")
        self.f_add_elements_to_top_right_frame()

        # =======================================================================================================================
        # Create the frame to hold the buttons
        self.buttons_frame = tk.Frame(frame_inside_canvas, bd=2, relief="solid", bg="lightblue", height=150, width=500)
        self.buttons_frame.pack(fill="both", side="bottom", expand=True, padx=10, pady=10)
        self.f_add_elements_to_buttons_frame()
        
        # =======================================================================================================================
        # Update the scroll region of the canvas
        self.f_update_scroll_region()
        
        # Update the scrollregion of the canvas to match the size of the frame
        frame_inside_canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        
        # Default: scroll the canvas
        self.is_scrolling_canvas = True
        
        # Bind the mouse wheel event to the canvas (works anywhere on the window)
        self.canvas.bind_all("<MouseWheel>", self.f_on_mouse_wheel)
        
        # Monitor window size changes to toggle the scrollbar visibility
        self.master.bind("<Configure>", self.f_adjust_the_sizes_dynamically)
        
        # After everything is initialized, update scroll regions
        self.master.after(100, self.f_update_scroll_region)

    def f_adjust_the_sizes_dynamically(self, event):
        # =======================================================================================================================
        # Step: toggle_scrollbar_visibility
        # Check if the content of the canvas exceeds the window height
        bbox = self.canvas.bbox("all")
        if bbox:
            canvas_height = bbox[3]  # The bottommost coordinate of the content
            if canvas_height > self.master.winfo_height():
                # Show the scrollbar if content height is greater than window height
                self.v_scrollbar_of_frame_inside_canvas.pack(side="right", fill="y")
            else:
                # Hide the scrollbar if content height is less than window height
                self.v_scrollbar_of_frame_inside_canvas.pack_forget()
        # =======================================================================================================================
        # Step: Adjust the width of the frame inside the canvas dynamically.
        # Get the current width of the window and subtract 20
        new_width = self.master.winfo_width() - 0

        # Update the width of the frame_inside_canvas
        self.canvas.itemconfig(self.canvas_window, width=new_width)
        
        # =======================================================================================================================
        # Step: toggle_scrollbar_visibility
        # Check the width of the Treeview content against the available width
        treeview_width = sum(self.treeview.column(col, "width") for col in self.columns)  # Get the width of the Treeview content
        
        # Compare the total width of the Treeview with the width of the treeview_frame
        if treeview_width > self.treeview_frame.winfo_width():
            # Show the horizontal scrollbar if the Treeview content is wider than the frame
            self.h_scrollbar.pack(side="bottom", fill="x", padx=10, pady=5)
        else:
            # Hide the horizontal scrollbar if the Treeview content fits within the frame
            self.h_scrollbar.pack_forget()

    # def f_on_mouse_wheel(self, event):
    #     # Scroll the canvas depending on the wheel movement (event.delta)
    #     if event.delta > 0:  # Scroll up
    #         self.canvas.yview_scroll(-1, "units")
    #     else:  # Scroll down
    #         self.canvas.yview_scroll(1, "units")

    def f_enable_treeview_scroll(self, event):
        # Enable scrolling for the Treeview when the cursor enters the Treeview frame
        self.is_scrolling_canvas = False

    def f_enable_canvas_scroll(self, event):
        # Enable scrolling for the Canvas when the cursor leaves the Treeview frame
        self.is_scrolling_canvas = True

    def f_on_mouse_wheel(self, event):
        if self.is_scrolling_canvas:
            # Scroll the canvas depending on the wheel movement (event.delta)
            if event.delta > 0:  # Scroll up
                self.canvas.yview_scroll(-1, "units")
            else:  # Scroll down
                self.canvas.yview_scroll(1, "units")
        else:
            # Scroll the Treeview (vertical scroll) when the cursor is over it
            if event.delta > 0:  # Scroll up
                self.treeview.yview_scroll(-1, "units")
            else:  # Scroll down
                self.treeview.yview_scroll(1, "units")

    def f_add_elements_to_top_right_frame(self):      # Create 10 Entry fields for input
        # Create the refresh button in the top-right frame
        self.refresh_button = tk.Button(self.top_right_frame, text="Refresh", command=self.f_refresh_window)
        self.refresh_button.grid(row=0, column=0)

    def f_add_entries_to_entries_frame(self):      # Create 10 Entry fields for input
        self.entries = []
        for i in range(10):
            label = tk.Label(self.entries_frame, text=f"Field {i+1}:")
            label.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")
            entry = tk.Entry(self.entries_frame)
            entry.insert(0, f"Field {i+1}")  # Set the default value
            entry.grid(row=i+1, column=1, padx=10, pady=5)
            self.entries.append(entry)
    
    def f_add_elements_to_buttons_frame(self):       # Create buttons for CRUD operations
        create_button = tk.Button(self.buttons_frame, text="Create", command=self.f_create_entry)
        create_button.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        update_button = tk.Button(self.buttons_frame, text="Update", command=self.f_update_entry)
        update_button.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        delete_button = tk.Button(self.buttons_frame, text="Delete", command=self.f_delete_entry)
        delete_button.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        refresh_button = tk.Button(self.buttons_frame, text="Refresh", command=self.f_clear_entries)
        refresh_button.pack(side="left", fill="both", expand=True, padx=10, pady=10)
    
    # =======================================================================================================================
    # CRUD Functions to interact with the Treeview
    def f_create_entry(self):
        # Get the values from the entry fields
        values = [entry.get() for entry in self.entries]
        
        # Check if all fields are filled
        if all(values):
            # Insert a new row in the Treeview
            self.treeview.insert("", "end", values=values)
            
            # Clear entry fields
            self.f_clear_entries()

            # # Sort the Treeview after insertion (if needed)
            # self.f_sort_treeview()  # Sort after creating entry
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields")

    def f_update_entry(self):
        selected_item = self.treeview.selection()
        if selected_item:
            # Get the values from the entry fields
            values = [entry.get() for entry in self.entries]
            if all(values):
                self.treeview.item(selected_item, values=values)
                self.f_clear_entries()
                # self.f_sort_treeview()  # Sort after deletion
            else:
                messagebox.showwarning("Input Error", "Please fill in all fields")
        else:
            messagebox.showwarning("Selection Error", "Please select an item to update")

    def f_delete_entry(self):
        selected_item = self.treeview.selection()
        if selected_item:
            self.treeview.delete(selected_item)
            # self.f_sort_treeview()  # Sort after deletion
        else:
            # If no row is selected, delete the last row
            all_items = self.treeview.get_children()
            if all_items:
                last_item = all_items[-1]  # Get the last item
                self.treeview.delete(last_item)
            else:
                messagebox.showwarning("No Rows", "There are no rows to delete.")

    def f_select_item(self, event):
        selected_item = self.treeview.selection()
        if selected_item:
            values = self.treeview.item(selected_item, "values")
            for i in range(10):
                self.entries[i].delete(0, tk.END)
                self.entries[i].insert(0, values[i])
                
            # Update the label with the selected row's index
            row_index = self.treeview.index(selected_item)
            self.selected_row_label.config(text=f"Selected Row: {row_index + 1}")

    def f_clear_entries(self):
        for entry in self.entries:
            entry.delete(0, tk.END)
            entry.insert(0, f"Field {self.entries.index(entry)+1}")  # Set default value

    def f_sort_treeview(self):
        # Get all items in the Treeview
        items = self.treeview.get_children()

        # Filter out items where the first column is not a valid integer
        sorted_items = sorted(
            items, 
            key=lambda item: (
                int(self.treeview.item(item, "values")[0]) 
                if self.f_is_int(self.treeview.item(item, "values")[0]) 
                else float('inf')  # Assign a large number to non-numeric values
            )
        )
        
        # Clear all items in the Treeview
        for item in items:
            self.treeview.delete(item)

        # Insert the sorted items back into the Treeview
        for item in sorted_items:
            values = self.treeview.item(item, "values")
            self.treeview.insert("", "end", values=values)
    
    def f_is_int(self, value):
        try:
            int(value)  # Try to convert to an integer
            return True
        except ValueError:
            return False  # Return False if it fails
        
    def f_refresh_window(self):
        """Refresh the window by clearing the Treeview and entry fields"""
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        self.f_clear_entries()
        self.selected_row_label.config(text="Selected Row: 0")
        
    def f_add_elements_to_treeview_frame(self):
        self.columns = [f"Column {i+1}" for i in range(10)]
        
        # Create the Treeview
        self.treeview = ttk.Treeview(self.treeview_frame, columns=self.columns, show="headings", height=10)
        self.treeview.pack(fill="x", padx=10, pady=5)

        # Create headings for the Treeview columns
        self.treeview.heading(self.columns[0], text="STT")  # Set the first column header to "STT"
        for col in self.columns[1:]:
            self.treeview.heading(col, text=col)

        # Create headings for the Treeview columns
        for col in self.columns:
            self.treeview.heading(col, text=col)
            
        # Set column widths (optional)
        for i in range(10):
            self.treeview.column(self.columns[i], width=150)  # Adjust width as needed

        # Bind selection event to fill entries with the selected row's values
        self.treeview.bind("<ButtonRelease-1>", self.f_select_item)

        # Add a horizontal scrollbar
        self.h_scrollbar = tk.Scrollbar(self.treeview_frame, orient="horizontal", command=self.treeview.xview)
        self.treeview.configure(xscrollcommand=self.h_scrollbar.set)
        self.h_scrollbar.pack(fill="x", side="bottom", padx=10, pady=5)
        
        # Add a label to display selected row information
        self.selected_row_label = tk.Label(self.treeview_frame, text="Selected Row: 0", width=100)
        self.selected_row_label.pack(fill="x", side="bottom", padx=10, pady=5)

    def f_update_scroll_region(self):
        """Update the scroll region of the canvas to match the size of its content"""
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        # Ensure frame is at the top-left corner
        self.canvas.coords(self.canvas_window, 0, 0)