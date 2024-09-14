from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Function to get database connection
def get_db_connection():
    conn = sqlite3.connect('database/squires.db')
    conn.row_factory = sqlite3.Row  # So we can access rows as dictionaries
    return conn

# Route to initialize the database with multiple parking spots
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

# Initialize the database when the script runs
initialize_db()

# Route to update the parking spot (check in/out) dynamically based on the spot ID
@app.route('/spot/<int:spot_id>', methods=['GET', 'POST'])
def update_spot(spot_id):
    conn = get_db_connection()

    # Get the current status of the spot
    spot = conn.execute('SELECT * FROM parking_spots WHERE id = ?', (spot_id,)).fetchone()

    if request.method == 'POST':
        # Check-in: User marks the spot as occupied (status = 1)
        if request.form['action'] == 'checkin':
            new_status = 1  # Occupied
        # Check-out: User marks the spot as available (status = 0)
        else:
            new_status = 0  # Available

        # Update the parking spot status in the database
        conn.execute('UPDATE parking_spots SET status = ?, last_updated = ? WHERE id = ?',
                     (new_status, datetime.now(), spot_id))
        conn.commit()
        conn.close()

        # Redirect to confirmation or status page
        return redirect(url_for('spot_status', spot_id=spot_id))

    conn.close()
    return render_template('spot.html', spot=spot)

# Route to display the current status of the parking spot
@app.route('/spot/<int:spot_id>/status')
def spot_status(spot_id):
    conn = get_db_connection()
    spot = conn.execute('SELECT * FROM parking_spots WHERE id = ?', (spot_id,)).fetchone()
    conn.close()
    
    # Show the current status of the parking spot
    return f"Spot {spot_id} status: {'Occupied' if spot['status'] == 1 else 'Available'}"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
