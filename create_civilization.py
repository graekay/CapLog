import sqlite3
import random

def roll_d20():
    return random.randint(1, 20)

def determine_feature(table_name, feature_column):
    conn = sqlite3.connect('data/civilizations.db')
    c = conn.cursor()
    roll = roll_d20()
    c.execute(f"SELECT {feature_column} FROM {table_name} WHERE ? BETWEEN range_start AND range_end", (roll,))
    return c.fetchone()[0]

def generate_civilization():
    population = determine_feature('population_table', 'population')
    government = determine_feature('government_table', 'government')
    polity = determine_feature('polity_table', 'polity')
    society = determine_feature('society_table', 'society')
    religion = determine_feature('religion_table', 'religion')
    trade = determine_feature('trade_table', 'trade')

    return f"Population: {population}\nGovernment: {government}\nPolity: {polity}\nSociety: {society}\nReligion: {religion}\nTrade: {trade}"
