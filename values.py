import sqlite3
import random


conn = sqlite3.connect('data/values.db')
c = conn.cursor()

def values():
    conn = sqlite3.connect('data/values.db')
    c = conn.cursor()
    c.execute('SELECT value FROM values_table ORDER BY RANDOM() LIMIT 1')
    result = c.fetchone()
    conn.close()
    print(result)
    return result[0] if result else None
    

if __name__ == '__main__':
    values()