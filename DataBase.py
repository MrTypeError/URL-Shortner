import sqlite3


cur = sqlite3.connect('Newproject.db')

# cur = conn.cursor()

# cur.execute("""""")


cur.execute('''CREATE TABLE URL (
                UniqueID text PRIMARY KEY NOT NULL
                );''')

cur.execute("INSERT INTO URL VALUES ('12334' ) ")

cur.execute("SELECT * FROM URL")

#it takes a number as a  input and returns the nmber of Coloumns . 
# cur.fetchmany(5)

#It doesn't takes and argument it return the remaining coloumns .
# cur.fetchall()

curs = cur.cursor()

# curs.execute("""""")
print(curs.fetchone())


cur.commit()

cur.close()