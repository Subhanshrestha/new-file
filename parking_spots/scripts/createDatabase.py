import sqlite3

def initialize_db():
    conn = sqlite3.connect('database/squires.db')
    cursor = conn.cursor()
    
    # Create table for parking spots if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS parking_spots (
                        id INTEGER PRIMARY KEY,
                        status INTEGER DEFAULT 0,  -- 0 = available, 1 = taken
                        last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                      )''')
    conn.commit()
    conn.close()

# Initialize the database
initialize_db()
