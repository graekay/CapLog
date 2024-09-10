import sqlite3
import random
import math

def roll_d20():
    return random.randint(1, 20)

def get_from_table(cursor, table, roll):
    cursor.execute(f"SELECT * FROM {table} WHERE {roll} BETWEEN range_start AND range_end")
    return cursor.fetchone()

def generate_planets():
    conn = sqlite3.connect('Data/system.db')
    cursor = conn.cursor()

    output = ""

    num_of_planets = get_from_table(cursor, 'num_of_planets_table', roll_d20())[2]
    output += f"Num of planets: {num_of_planets}\n"

    primary_world_position = math.ceil(roll_d20() / 4)
    if primary_world_position > num_of_planets:
        primary_world_position = num_of_planets

    primary_world_type = get_from_table(cursor, 'primary_world_table', roll_d20())[2]
    output += f"Primary World: class {primary_world_type}\n"

    for i in range(1, primary_world_position):
        inner_world_type = get_from_table(cursor, 'inner_worlds_table', roll_d20())[2]
        output += f"Inner World {i}: class {inner_world_type}\n"

    for i in range(primary_world_position + 1, num_of_planets + 1):
        outer_world_type = get_from_table(cursor, 'outer_worlds_table', roll_d20())[2]
        output += f"Outer World {i - primary_world_position}: class {outer_world_type}\n"

    conn.close()

    return output

