import sqlite3
import random

class System:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def roll_dice(self, sides):
        return random.randint(1, sides)

    def get_from_table(self, table_name, column_name, dice_roll):
        self.cursor.execute(f"SELECT {column_name} FROM {table_name} WHERE ? BETWEEN range_start AND range_end", (dice_roll,))
        return self.cursor.fetchone()[0]

    def generate_star(self):
        spectral_class_roll = self.roll_dice(20)
        spectral_class = self.get_from_table('spectral_class_table', 'spectral_class', spectral_class_roll)
        print(f"Rolled {spectral_class_roll} on spectral_class_table, got spectral class {spectral_class}")
        if spectral_class_roll == 20:
            special_spectral_class_roll = self.roll_dice(20)
            spectral_class = self.get_from_table('special_spectral_class_table', 'special_spectral_class', special_spectral_class_roll)
            print(f"Rolled {special_spectral_class_roll} on special_spectral_class_table, got special spectral class {spectral_class}")
            if 16 <= special_spectral_class_roll <= 20:
                spatial_phenomena = self.generate_spatial_phenomena()
                print(f"Rolled a spatial phenomena: {spatial_phenomena}")
                return {"class": spectral_class, "luminosity": self.generate_luminosity_class(), "phenomena": spatial_phenomena}
        return {"class": spectral_class, "luminosity": self.generate_luminosity_class()}

    def generate_luminosity_class(self):
        return self.get_from_table('luminosity_class_table', 'luminosity_class', self.roll_dice(20))

    def generate_spatial_phenomena(self):
            dice_roll = self.roll_dice(20)
            column = f'option_{chr(96 + self.roll_dice(5))}'
            print(f"Dice roll: {dice_roll}, column: {column}")
            self.cursor.execute(f"SELECT {column} FROM spatial_phenomena_table WHERE ? BETWEEN range_start AND range_end", (dice_roll,))
            phenomena = self.cursor.fetchone()
            print(f"Phenomena: {phenomena}")
            if phenomena is not None:
                return phenomena[0]
            else:
                return "No phenomena found"

    def generate_system(self):
        return self.generate_star()

# Usage
#system = System('data/system.db')
#print(system.generate_system())
