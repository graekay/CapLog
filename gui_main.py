import tkinter as tk
from encounter import generate_encounter

# Create the main window
root = tk.Tk()

# Create the first frame for the buttons
frame1 = tk.Frame(root)
frame1.pack(side=tk.LEFT)

# Create three buttons for the first frame
button1 = tk.Button(frame1, text="Button 1", command=lambda: display_result(generate_encounter()))
button2 = tk.Button(frame1, text="Button 2")
button3 = tk.Button(frame1, text="Button 3")

# Pack the buttons into the first frame
button1.pack(side=tk.TOP)
button2.pack(side=tk.TOP)
button3.pack(side=tk.TOP)

# Create the second frame for the result display
frame2 = tk.Frame(root)
frame2.pack(side=tk.LEFT)

# Create a label to display the result
result_label = tk.Label(frame2, text="")
result_label.pack()

# Function to display the result of generate_encounter() in the label
def display_result(result):
    result_label.config(text=result)

# Run the main loop
root.mainloop()
