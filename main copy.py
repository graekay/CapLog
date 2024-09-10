import tkinter as tk
from tkinter import filedialog, Text, font
app = tk.Tk()
app.title("Captain's Log Generators")

text_area = Text(app, wrap='word')
text_area.pack(side=tk.RIGHT, expand='yes', fill=tk.BOTH)
text_area.config(state='disabled')

def insert_text(text, bold=False, underline=False, italic=False, family=None, size=None):
    font_weight = "bold" if bold else "normal"
    font_slant = "italic" if italic else "roman"
    font_underline = 1 if underline else 0
    font = tk.font.Font(weight=font_weight, slant=font_slant, underline=font_underline, family=family, size=size)
    text_area.tag_configure("custom", font=font)
    text_area.insert(tk.END, text, "custom")


def new_file():
    text_area.config(state='normal')
    text_area.delete(1.0, tk.END)
    text_area.config(state='disable')

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.config(state='normal')
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
            text_area.config(state='disabled')

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))


def insert_wip():
    text_area.config(state='normal')
    #text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, "WIP\n")
    text_area.config(state='disabled')

def insert_encounter():
    from create_encounter import Encounters
    encounter_generator = Encounters('data/encounter.db')
    encounter = encounter_generator.generate_encounter()
    text_area.config(state='normal')
    #text_area.delete(1.0, tk.END)
    insert_text("Encounter\n", underline=True, family="Arial", size=12)
    text_area.insert(tk.END, f"Type: {encounter['type']}\nEncounter: {encounter['encounter']}\n")
    text_area.config(state='disabled')

def insert_mission():
    from create_mission import Mission
    mission_generator = Mission('data/missions.db')
    mission_generator.generate()
    mission = mission_generator.get_report()
    text_area.config(state='normal')
    #text_area.delete(1.0, tk.END)
    insert_text("Mission\n", underline=True, family="Arial", size=12)
    text_area.insert(tk.END, f"Type: {mission['Type']}\nDetails: {mission['Details']}\nInciting Incident: {mission['Inciting Incident']}\n")
    if mission['Advantage']:
        text_area.insert(tk.END, f"Advantage: {mission['Advantage']}\n")
    if mission['Complication']:
        text_area.insert(tk.END, f"Complication: {mission['Complication']}\n")
    text_area.config(state='disabled')

def insert_system():
    from create_system import System
    system_generator = System('data/system.db')
    system = system_generator.generate_system()
    text_area.config(state='normal')
    insert_text("System\n", underline=True, family="Arial", size=12)
    if 'class' in system:
        text_area.insert(tk.END, f"Star Class: {system['class']}\nLuminosity Class: {system['luminosity']}\n")
        if 'phenomena' in system:
            text_area.insert(tk.END, f"Spatial Phenomena: {system['phenomena']}\n")
    else:
        text_area.insert(tk.END, f"Spatial Phenomena: {system['phenomena']}\n")
    text_area.config(state='disabled')

def insert_planet():
    from create_planets import generate_planets
    text_area.config(state='normal')
    insert_text("Planets\n", underline=True, family="Arial", size=12)
    text_area.insert(tk.END, generate_planets())
    text_area.config(state='disabled')


button_frame = tk.Frame(app)
button_frame.pack(side=tk.LEFT, fill=tk.Y)
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_rowconfigure(0, weight=0)
button_frame.grid_rowconfigure(1, weight=0)
button_frame.grid_rowconfigure(2, weight=0)

button1 = tk.Button(button_frame, text="Character", command=insert_wip)
button1.grid(row=0, column=0, sticky="nsew")

button2 = tk.Button(button_frame, text="Ship", command=insert_wip)
button2.grid(row=1, column=0, sticky="nsew")

button3 = tk.Button(button_frame, text="Crew", command=insert_wip)
button3.grid(row=2, column=0, sticky="nsew")

button4 = tk.Button(button_frame, text="Mission", command=insert_mission)
button4.grid(row=3, column=0, sticky="nsew")

button5 = tk.Button(button_frame, text="Encounter", command=insert_encounter)
button5.grid(row=4, column=0, sticky="nsew")

button6 = tk.Button(button_frame, text="System", command=insert_system)
button6.grid(row=5, column=0, sticky="nsew")

button7 = tk.Button(button_frame, text="Planet", command=insert_planet)
button7.grid(row=6, column=0, sticky="nsew")

button8 = tk.Button(button_frame, text="Civilization", command=insert_wip)
button8.grid(row=7, column=0, sticky="nsew")

menu_bar = tk.Menu(app)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

app.config(menu=menu_bar)
app.mainloop()
