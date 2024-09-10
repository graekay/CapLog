import sqlite3
import random
import json
import os

class Encounters:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()

    def roll_d20(self):
        return random.randint(1, 20)

    def get_data(self, table):
        self.c.execute(f'SELECT * FROM {table}')
        return self.c.fetchall()

    def determine_type(self, type_roll):
        self.c.execute('Select * FROM encounter_type WHERE ? BETWEEN range_start AND range_end', (type_roll,))
        return self.c.fetchone()

    def determine_encounter(self, type_id, encounter_roll):
        self.c.execute('SELECT encounter FROM encounters WHERE type_id = ? AND  id =?', (type_id, encounter_roll))
        return self.c.fetchone()[0]

    def generate_encounter(self):
        type_roll = self.roll_d20()
        type_id, _, _, type = self.determine_type(type_roll)
        encounter_roll = self.roll_d20()
        encounter = self.determine_encounter(type_id, encounter_roll)
        return {"type": type, "encounter": encounter}