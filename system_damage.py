import sqlite3
import random

# Connect to the SQLite database
conn = sqlite3.connect('data/ship_damage.db')
c = conn.cursor()

# Roll a 20-sided die
def roll_d20():
    return random.randint(1, 20)

# Retrieve data from the database
def get_data(table):
    c.execute(f'SELECT * FROM {table}')
    return c.fetchall()

def determine_system(system_roll):
    c.execute('Select system FROM ship_system WHERE ? BETWEEN range_start AND range_end', (system_roll,))
    return c.fetchone()[0]

# Determine severity based on roll
def determine_severity(roll):
    c.execute('SELECT * FROM damage_severity WHERE ? BETWEEN range_start AND range_end', (roll,))
    return c.fetchone()

# Determine details based on severity_id and roll
def determine_details(severity_id, roll):
    c.execute('SELECT details FROM severity_details WHERE severity_id = ? AND ? BETWEEN range_start AND range_end', (severity_id, roll))
    return c.fetchone()[0]

# Generate a damage report
def generate_damage_report():
    system_roll = roll_d20()
    system = determine_system(system_roll)
    roll = roll_d20()
    severity_id, _, _, severity = determine_severity(roll)
    detail_roll = roll_d20()
    details = determine_details(severity_id, detail_roll)
    return f"System: {system} \nSeverity: {severity} {details}"

while True:
    print(generate_damage_report())
    response = input("Reroll? (y/n): ")
    if response.lower() != "y":
        break

# Print a damage report
print(generate_damage_report())

# Close the connection to the database
conn.close()
