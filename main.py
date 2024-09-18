import sqlite3

# Connect to the SQLite database (creates concerts.db if it doesn't exist)
def connect_db():
    conn = sqlite3.connect('concerts.db')  # This will create concerts.db if it doesn't exist
    return conn

# Create tables by executing the commands in createTable.sql
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # Read and execute SQL commands from createTable.sql
    with open('createTable.sql', 'r') as f:
        create_table_sql = f.read()

    cursor.executescript(create_table_sql)
    conn.commit()
    conn.close()

# Insert sample data by executing the commands in insertData.sql
def insert_data():
    conn = connect_db()
    cursor = conn.cursor()

    # Read and execute SQL commands from insertData.sql
    with open('insertData.sql', 'r') as f:
        insert_data_sql = f.read()

    cursor.executescript(insert_data_sql)
    conn.commit()
    conn.close()

# Example function: Get the band for a specific concert
def get_band_for_concert(concert_id):
    conn = connect_db()
    cursor = conn.cursor()

    # SQL query to get the band details for a concert
    cursor.execute('''
        SELECT bands.name, bands.hometown
        FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        WHERE concerts.id = ?;
    ''', (concert_id,))
    
    band = cursor.fetchone()
    conn.close()
    return band

# Example function: Get the venue for a specific concert
def get_venue_for_concert(concert_id):
    conn = connect_db()
    cursor = conn.cursor()

    # SQL query to get the venue details for a concert
    cursor.execute('''
        SELECT venues.title, venues.city
        FROM venues
        JOIN concerts ON venues.id = concerts.venue_id
        WHERE concerts.id = ?;
    ''', (concert_id,))
    
    venue = cursor.fetchone()
    conn.close()
    return venue

# Main execution
if __name__ == "__main__":
    # Step 1: Create tables by executing SQL from createTable.sql
    create_tables()

    # Step 2: Insert sample data from insertData.sql
    insert_data()

    # Step 3: Fetch and display band and venue for concert with id 1
    band = get_band_for_concert(1)
    print(f"Concert 1 Band: {band}")

    venue = get_venue_for_concert(1)
    print(f"Concert 1 Venue: {venue}")