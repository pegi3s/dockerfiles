import tkinter as tk
from tkinter import ttk
from manageDocker import delete_docker_image, get_docker_images, is_image_in_use

# Sort state tracking
sort_column = None
sort_reverse = False

def parse_size_to_bytes(size_str):
    """Convert size string (e.g., '359MB', '1GB', '500KB') to bytes"""
    size_str = size_str.strip().upper()
    
    # Define unit multipliers (sorted by length descending to match longer units first)
    units = [
        ('TB', 1024 ** 4),
        ('GB', 1024 ** 3),
        ('MB', 1024 ** 2),
        ('KB', 1024),
        ('B', 1),
    ]
    
    # Extract number and unit
    for unit, multiplier in units:
        if size_str.endswith(unit):
            try:
                number = float(size_str[:-len(unit)])
                return number * multiplier
            except ValueError:
                return 0
    
    # If no unit found, try to parse as plain number
    try:
        return float(size_str)
    except ValueError:
        return 0

def sort_treeview(column):
    """Sort treeview by column when header is clicked"""
    global sort_column, sort_reverse
    
    # If clicking the same column, toggle sort order
    if sort_column == column:
        sort_reverse = not sort_reverse
    else:
        sort_column = column
        sort_reverse = False
    
    # Get all items from treeview
    items = [(my_tree.set(item, column), item) for item in my_tree.get_children()]
    
    # Sort items based on column type
    if column == "Size":
        # For Size column, convert to bytes first for proper comparison
        items.sort(key=lambda x: parse_size_to_bytes(x[0]), reverse=sort_reverse)
    else:
        # For other columns, try numeric sort first, fall back to string sort
        try:
            items.sort(key=lambda x: float(x[0]), reverse=sort_reverse)
        except ValueError:
            items.sort(key=lambda x: x[0], reverse=sort_reverse)
    
    # Rearrange items in sorted order
    for index, (val, item) in enumerate(items):
        my_tree.move(item, "", index)

def show_toast(instruction):
    toast = tk.Toplevel()
    toast.title("Toast")
    toast.geometry("300x100")
    tk.Label(toast, text=instruction, font=("Helvetica", 12)).pack(pady=20)
    toast.after(2000, toast.destroy)  # Close the toast after 2 seconds (2000 milliseconds)

def delete_item(item_id):
    my_tree.delete(item_id)

def on_delete_button_click(item_id):
    delete_item(item_id)


def delete_selected_item():
    selected_items = my_tree.selection()
    for item_id in selected_items:
        image_id = my_tree.item(item_id, "values")[2]  # Get the Image ID from the selected item
        if delete_docker_image(image_id):
            print(f"Deleted image {image_id} successfully.")
            delete_item(item_id)  # Delete the item from the Treeview if the image was deleted

def refresh_treeview():
    # Clear the existing items in the Treeview
    for item in my_tree.get_children():
        my_tree.delete(item)

    # Fetch Docker images and populate the Treeview
    docker_images = get_docker_images()
    for image in docker_images:
        status = is_image_in_use(image["IMAGE ID"])
        item_id = my_tree.insert("", "end", values=(image["REPOSITORY"], image["TAG"], image["IMAGE ID"], image["CREATED"], image["SIZE"], status))

def delete_unused_images():
    docker_images = get_docker_images()
    for image in docker_images:
        status = is_image_in_use(image["IMAGE ID"])
        if not status:  # If the image is not in use, delete it
            delete_docker_image(image["IMAGE ID"])

    refresh_treeview()  # Refresh the Treeview after deleting unused images

# Create the main window
window = tk.Tk()
window.title("Manage Docker Images")
window.geometry("1000x500")

# Add text above the Treeview
title_label = tk.Label(window, text="Manage Docker Images", font=("Helvetica", 25))
title_label.pack(pady=20)

# Create a frame to hold the Treeview and the vertical scrollbar
tree_frame = tk.Frame(window)
tree_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# Create a Treeview for displaying items
my_tree = ttk.Treeview(tree_frame, columns=("Name", "Tag", "ID", "Date", "Size", "Status"), show="headings", height=14)
my_tree.heading("Name", text="Name")
my_tree.heading("Tag", text="Tag")
my_tree.heading("ID", text="Image ID")
my_tree.heading("Date", text="Date")
my_tree.heading("Size", text="Size")
my_tree.heading("Status", text="Status")
my_tree.column("Name", width=200, anchor="center")
my_tree.column("Tag", width=200, anchor="center")
my_tree.column("ID", width=150, anchor="center")
my_tree.column("Date", width=150, anchor="center")
my_tree.column("Size", width=100, anchor="center")
my_tree.column("Status", width=100, anchor="center")

# Bind sorting to column headers
my_tree.heading("Name", command=lambda: sort_treeview("Name"))
my_tree.heading("Tag", command=lambda: sort_treeview("Tag"))
my_tree.heading("Size", command=lambda: sort_treeview("Size"))
my_tree.heading("Status", command=lambda: sort_treeview("Status"))

# Fetch Docker images and populate the Treeview
docker_images = get_docker_images()
for image in docker_images:
    status = is_image_in_use(image["IMAGE ID"])
    item_id = my_tree.insert("", "end", values=(image["REPOSITORY"], image["TAG"], image["IMAGE ID"], image["CREATED"], image["SIZE"], status))

# Create a vertical scrollbar
vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=my_tree.yview)
my_tree.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")

# Increase the width of the entire treeview
my_tree.pack(expand=True, fill="both")

# Create a frame for buttons at the bottom
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

refreshButton = tk.Button(button_frame, text="Refresh", command=refresh_treeview)
deleteUnusedImagesButton = tk.Button(button_frame, text="Delete Unused Images", command=delete_unused_images)
delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_selected_item)

refreshButton.pack(side="left", padx=10)
deleteUnusedImagesButton.pack(side="left", padx=10)
delete_button.pack(side="left", padx=10)


window.mainloop()
