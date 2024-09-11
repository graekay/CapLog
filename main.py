import tkinter as tk
from tkinter import filedialog, Text, font

app = tk.Tk()
app.title("Captain's Log Generators")
app.geometry("800x800")

# Create a frame for the buttons
button_frame = tk.Frame(app)
button_frame.pack(side=tk.LEFT, fill=tk.Y)

# Create a canvas and a scroll bar for the main window
canvas = tk.Canvas(app)
scrollbar = tk.Scrollbar(app, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Pack the canvas and scroll bar into the main window
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Create a frame to hold all text areas
text_frame = tk.Frame(canvas)

# Pack the text frame into the canvas
canvas.create_window((0, 0), window=text_frame, anchor="nw")

# Function to create a text area with a label
def create_text_area(label_text):
    label = tk.Label(text_frame, text=label_text)
    label.pack(pady=2)

    # Create a frame to hold the text area and scroll bar
    frame = tk.Frame(text_frame)
    frame.pack(pady=2, fill=tk.BOTH, expand=True)

    # Create a scroll bar
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create the text area
    text_area = Text(frame, wrap='word', height=1, yscrollcommand=scrollbar.set, width=80)
    text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Configure the scroll bar to work with the text area
    scrollbar.config(command=text_area.yview)

    text_area.config(state='disabled')

    def update_height(event):
        text_area.config(height=text_area.index('end -1 line').split('.')[0])

    text_area.bind('<Configure>', update_height)

    return text_area

# Create text areas for each function
#character_text_area = create_text_area("Character")
#ship_text_area = create_text_area("Ship")
#crew_text_area = create_text_area("Crew")
mission_text_area = create_text_area("Mission")
encounter_text_area = create_text_area("Encounter")
system_text_area = create_text_area("System")
planet_text_area = create_text_area("Planet")
civilization_text_area = create_text_area("Civilization")

# Pack the text areas into the text frame
#character_text_area.pack(pady=2)
#ship_text_area.pack(pady=2)
#crew_text_area.pack(pady=2)
mission_text_area.pack(pady=2)
encounter_text_area.pack(pady=2)
system_text_area.pack(pady=2)
planet_text_area.pack(pady=2)
civilization_text_area.pack(pady=2)

# Update the scroll region of the canvas
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

text_frame.bind("<Configure>", on_configure)

# Function to insert text into a text area
def insert_text(text_area, text, bold=False, underline=False, italic=False, family=None, size=None):
    font_weight = "bold" if bold else "normal"
    font_slant = "italic" if italic else "roman"
    font_underline = 1 if underline else 0
    font = tk.font.Font(weight=font_weight, slant=font_slant, underline=font_underline, family=family, size=size)
    text_area.tag_configure("custom", font=font)
    text_area.insert(tk.END, text, "custom")
    text_area.update_idletasks()  # Update the widget to get the correct height
    text_area.config(height=text_area.index('end -1 line').split('.')[0])  # Set the height to the number of lines

# Function to update the height of a text area
def update_height(text_area):
    text_area.config(height=text_area.index('end -1 line').split('.')[0])

# Modify your insert functions to use the correct text area
#def insert_character():
#    text_area = character_text_area
#    text_area.config(state='normal')
#    text_area.delete(1.0, tk.END)
#    text_area.insert(tk.END, "WIP\n")
#    text_area.update_idletasks()  # Update the widget to get the correct height
#    update_height(text_area)
#    text_area.config(state='disabled')

#def insert_ship():
#    text_area = ship_text_area
#    text_area.config(state='normal')
#    text_area.delete(1.0, tk.END)
#    text_area.insert(tk.END, "WIP\n")
#    text_area.update_idletasks()  # Update the widget to get the correct height
#    update_height(text_area)
#    text_area.config(state='disabled')

#def insert_crew():
#    text_area = crew_text_area
#    text_area.config(state='normal')
#    text_area.delete(1.0, tk.END)
#    text_area.insert(tk.END, "WIP\n")
#    text_area.update_idletasks()  # Update the widget to get the correct height
#    update_height(text_area)
#    text_area.config(state='disabled')

def insert_mission():
    from create_mission import Mission
    mission_generator = Mission('data/missions.db')
    mission_generator.generate()
    mission = mission_generator.get_report()
    text_area = mission_text_area
    text_area.config(state='normal')
    text_area.delete(1.0, tk.END)
    insert_text(text_area, "Mission\n", underline=True, family="Arial", size=12)
    text_area.insert(tk.END, f"Type: {mission['Type']}\nDetails: {mission['Details']}\nInciting Incident: {mission['Inciting Incident']}\n")
    if mission['Advantage']:
        text_area.insert(tk.END, f"Advantage: {mission['Advantage']}\n")
    if mission['Complication']:
        text_area.insert(tk.END, f"Complication: {mission['Complication']}\n")
    text_area.update_idletasks()  # Update the widget to get the correct height
    update_height(text_area)
    text_area.config(state='disabled')

def insert_encounter():
    from create_encounter import Encounters
    encounter_generator = Encounters('data/encounter.db')
    encounter = encounter_generator.generate_encounter()
    text_area = encounter_text_area
    text_area.config(state='normal')
    text_area.delete(1.0, tk.END)
    insert_text(text_area, "Encounter\n", underline=True, family="Arial", size=12)
    text_area.insert(tk.END, f"Type: {encounter['type']}\nEncounter: {encounter['encounter']}\n")
    text_area.update_idletasks()  # Update the widget to get the correct height
    update_height(text_area)
    text_area.config(state='disabled')

def insert_system():
    from create_system import System
    system_generator = System('data/system.db')
    system = system_generator.generate_system()
    text_area = system_text_area
    text_area.config(state='normal')
    text_area.delete(1.0, tk.END)
    insert_text(text_area, "System\n", underline=True, family="Arial", size=12)
    if 'class' in system:
        text_area.insert(tk.END, f"Star Class: {system['class']}\nLuminosity Class: {system['luminosity']}\n")
        if 'phenomena' in system:
            text_area.insert(tk.END, f"Spatial Phenomena: {system['phenomena']}\n")
    else:
        text_area.insert(tk.END, f"Spatial Phenomena: {system['phenomena']}\n")
    text_area.update_idletasks()  # Update the widget to get the correct height
    update_height(text_area)
    text_area.config(state='disabled')

def insert_planet():
    from create_planets import generate_planets
    text_area = planet_text_area
    text_area.config(state='normal')
    text_area.delete(1.0, tk.END)
    insert_text(text_area, "Planets\n", underline=True, family="Arial", size=12)
    text_area.insert(tk.END, generate_planets())
    text_area.update_idletasks()  # Update the widget to get the correct height
    update_height(text_area)
    text_area.config(state='disabled')

def insert_civilization():
    from create_civilization import generate_civilization
    text_area = civilization_text_area
    text_area.config(state='normal')
    text_area.delete(1.0, tk.END)
    insert_text(text_area, "Civilization\n", underline=True, family="Arial", size=12)
    text_area.insert(tk.END, generate_civilization())
    text_area.update_idletasks()  # Update the widget to get the correct height
    update_height(text_area)
    text_area.config(state='disabled')


# Create buttons for each function
#button1 = tk.Button(button_frame, text="Character", command=insert_character, width=10)
#button1.pack(pady=2)

#button2 = tk.Button(button_frame, text="Ship", command=insert_ship, width=10)
#button2.pack(pady=2)

#button3 = tk.Button(button_frame, text="Crew", command=insert_crew, width=10)
#button3.pack(pady=2)

button4 = tk.Button(button_frame, text="Mission", command=insert_mission, width=10)
button4.pack(pady=2)

button5 = tk.Button(button_frame, text="Encounter", command=insert_encounter, width=10)
button5.pack(pady=2)

button6 = tk.Button(button_frame, text="System", command=insert_system, width=10)
button6.pack(pady=2)

button7 = tk.Button(button_frame, text="Planet", command=insert_planet, width=10)
button7.pack(pady=2)

button8 = tk.Button(button_frame, text="Civilization", command=insert_civilization, width=10)
button8.pack(pady=2)

app.mainloop()
