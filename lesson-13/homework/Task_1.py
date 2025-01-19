import sqlite3

CREATE = "CREATE TABLE IF NOT EXISTS Roster(Name TEXT, Species TEXT, Age INT);"
INSERT = """
Insert into Roster Values
('Benjamin Sisko', 'Human', 40),
('Jadzia Dax', 'Trill', 300),
('Kira Nerys', 'Bajoran', 29);
"""
UPDATE_DATA = "UPDATE Roster SET name = 'Ezri Dax' WHERE name = 'Jadzia Dax';"
QUERY_DATA = "SELECT Name, Age FROM Roster WHERE Species = 'Bajoran';"
DELETE_DATA = "DELETE FROM Roster WHERE Age > 100;"
BONUS_TASK = """
ALTER TABLE Roster ADD COLUMN Rank TEXT;

UPDATE Roster SET Rank = 'Captain' WHERE Name = 'Benjamin Sisko';
UPDATE Roster SET Rank = 'Lieutenant' WHERE Name = 'Ezri Dax';
UPDATE Roster SET Rank = 'Major' WHERE Name = 'Kira Nerys';
"""
ADVANCED_QUERY = "SELECT * FROM Roster ORDER BY Age DESC;"

with sqlite3.connect("roster.db") as roster:
    cursor = roster.cursor()
    cursor.execute(CREATE)
    cursor.execute(INSERT)
    cursor.execute(UPDATE_DATA)
    cursor.execute(QUERY_DATA)
    cursor.execute(DELETE_DATA)
    cursor.executescript(BONUS_TASK)
    cursor.execute(ADVANCED_QUERY)