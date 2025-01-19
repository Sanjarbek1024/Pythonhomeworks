import sqlite3

# SQL Commands
CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
);
"""

INSERT_DATA = """
INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES
('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
('1984', 'George Orwell', 1949, 'Dystopian'),
('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic');
"""

UPDATE_YEAR = "UPDATE Books SET Year_Published = 1950 WHERE Title = '1984';"

QUERY_DYSTOPIAN = "SELECT Title, Author FROM Books WHERE Genre = 'Dystopian';"
DELETE_BEFORE_1950 = "DELETE FROM Books WHERE Year_Published < 1950;"

BONUS_TASK = """
ALTER TABLE Books ADD COLUMN Rating REAL;

UPDATE Books SET Rating = 4.8 WHERE Title = 'To Kill a Mockingbird';
UPDATE Books SET Rating = 4.7 WHERE Title = '1984';
UPDATE Books SET Rating = 4.5 WHERE Title = 'The Great Gatsby';
"""

ADVANCED_QUERY = "SELECT * FROM Books ORDER BY Year_Published ASC;"

# Function to print query results
def print_results(description, cursor):
    results = cursor.fetchall()
    print(f"\n{description}:")
    for row in results:
        print(row)

# Main Program
try:
    with sqlite3.connect("library.db") as library:
        cursor = library.cursor()

        # Database Creation:
        cursor.execute(CREATE_TABLE)

        # Insert Data:
        cursor.execute(INSERT_DATA)

        # Update Data:
        cursor.execute(UPDATE_YEAR)

        # Query Data:
        cursor.execute(QUERY_DYSTOPIAN)
        print_results("Dystopian Books", cursor)

        # Delete Data:
        cursor.execute(DELETE_BEFORE_1950)

        # Add a new column called Rating to the Books table and update the data with the following values:
        cursor.executescript(BONUS_TASK)

        # Retrieve all books sorted by Year_Published in ascending order
        cursor.execute(ADVANCED_QUERY)
        print_results("Books Sorted by Year Published", cursor)

except sqlite3.Error as e:
    print(f"Database error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
