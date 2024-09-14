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

    # Insert 3 parking spots with QR IDs if they don't already exist
    cursor.execute('INSERT OR IGNORE INTO parking_spots (id, status) VALUES (1, 0)')
    cursor.execute('INSERT OR IGNORE INTO parking_spots (id, status) VALUES (2, 0)')
    cursor.execute('INSERT OR IGNORE INTO parking_spots (id, status) VALUES (3, 0)')
    
    conn.commit()
    conn.close()

# Initialize the database with 3 spots
initialize_db()
