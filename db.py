import sqlite3

con = sqlite3.connect("detectivebot.db")

cursor = con.cursor()

# cursor.execute("""CREATE TABLE suspected
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 # name TEXT)
#             """)
#
# cursor.execute("""CREATE TABLE hint
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 description TEXT,
#                 suspected_id INTEGER,
#                 FOREIGN KEY (suspected_id) REFERENCES suspected(id))
#             """)

# suspected_people = [("Леди Сотби",), ("Джеймс Реддингтон",), ("Роуз Реддингтон",), ("Реджинальда Вебстер",), ("Владелец",), ("Теодор Рив",)]
# cursor.executemany("INSERT INTO suspected (name) VALUES (?)", suspected_people)

con.commit()

