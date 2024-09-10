import sqlite3
import random

# Connect to the database
conn = sqlite3.connect('data/missions.db')
cursor = conn.cursor()

class Mission:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.type = None
        self.details = None
        self.inciting_incident = None
        self.advantage = None
        self.complication = None

    def generate(self):
        # Roll a d20 to get the type
        self.cursor.execute('SELECT type FROM mission_type ORDER BY RANDOM() LIMIT 1')
        self.type = self.cursor.fetchone()[0]

        # Roll a d20 to get the details based on the type
        self.cursor.execute('SELECT details FROM mission_details WHERE type_id = (SELECT id FROM mission_type WHERE type = ?) ORDER BY RANDOM() LIMIT 1', (self.type,))
        self.details = self.cursor.fetchone()[0]

        # Roll a d20 to get the inciting incident
        self.cursor.execute('SELECT incident FROM mission_incident ORDER BY RANDOM() LIMIT 1')
        incident = self.cursor.fetchone()[0]

        # Roll a d20 to get the theme
        self.cursor.execute('SELECT theme FROM mission_theme ORDER BY RANDOM() LIMIT 1')
        theme = self.cursor.fetchone()[0]

        self.inciting_incident = incident + ' ' + theme

        # Roll a d20 to get the advantage or complication
        roll = random.randint(1, 20)
        if roll % 2 == 0:
            self.cursor.execute('SELECT advantage FROM advantages ORDER BY RANDOM() LIMIT 1')
            self.advantage = self.cursor.fetchone()[0]
            self.complication = None
        else:
            self.cursor.execute('SELECT complication FROM complications ORDER BY RANDOM() LIMIT 1')
            self.complication = self.cursor.fetchone()[0]
            self.advantage = None
    
    def generate_mission(self):
        self.generate()
        return self.get_report()

    def get_report(self):
        report = {
            'Type': self.type,
            'Details': self.details,
            'Inciting Incident': self.inciting_incident,
            'Advantage': self.advantage,
            'Complication': self.complication
        }
        if self.advantage:
            report['Advantage'] = self.advantage
        if self.complication:
            report['Complication'] = self.complication
        return report

# Generate a mission
mission = Mission('data/missions.db')
mission.generate_mission()

# Get the mission report
mission_report = mission.get_report()
