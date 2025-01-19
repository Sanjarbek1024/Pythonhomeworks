import sqlite3

# SQL Commands
CREATE = """
CREATE TABLE IF NOT EXISTS Roster(
    Name TEXT,
    Species TEXT,
    Age INT
);
"""
INSERT = """
INSERT INTO Roster (Name, Species, Age) VALUES
('Benjamin Sisko', 'Human', 40),
('Jadzia Dax', 'Trill', 300),
('Kira Nerys', 'Bajoran', 29);
"""
UPDATE_DATA = "UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax';"
QUERY_DATA = "SELECT Name, Age FROM Roster WHERE Species = 'Bajoran';"
DELETE_DATA = "DELETE FROM Roster WHERE Age > 100;"
BONUS_TASK = """
ALTER TABLE Roster ADD COLUMN Rank TEXT;

UPDATE Roster SET Rank = 'Captain' WHERE Name = 'Benjamin Sisko';
UPDATE Roster SET Rank = 'Lieutenant' WHERE Name = 'Ezri Dax';
UPDATE Roster SET Rank = 'Major' WHERE Name = 'Kira Nerys';
"""
ADVANCED_QUERY = "SELECT * FROM Roster ORDER BY Age DESC;"

# Function to print query results
def print_results(description, cursor):
    results = cursor.fetchall()
    print(f"\n{description}:")
    for row in results:
        print(row)

# Main Program
try:
    with sqlite3.connect("roster.db") as roster:
        cursor = roster.cursor()

        # Step 1: Create the table
        cursor.execute(CREATE)

        # Step 2: Insert data into the table
        cursor.execute(INSERT)

        # Step 3: Update Jadzia Dax to Ezri Dax
        cursor.execute(UPDATE_DATA)

        # Step 4: Query Bajoran characters
        cursor.execute(QUERY_DATA)
        print_results("Bajoran Characters", cursor)

        # Step 5: Delete characters aged over 100
        cursor.execute(DELETE_DATA)

        # Step 6: Add Rank column and update data
        cursor.executescript(BONUS_TASK)

        # Step 7: Query all characters sorted by Age in descending order
        cursor.execute(ADVANCED_QUERY)
        print_results("All Characters (Sorted by Age)", cursor)

except sqlite3.Error as e:
    print(f"Database error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")