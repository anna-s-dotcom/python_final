import sqlite3

# con = sqlite3.connect('first.db')
#
# c = con.cursor()

# try:
#     c.execute("CREATE TABLE person(name TEXT, telefon TEXT)")
# except:
#     print('Table already exists')

# erstellen einer tabelle in der datenbank
# c.execute("""CREATE TABLE IF NOT EXISTS person(name TEXT, telefon TEXT)""")


############## CREATE ######################

# # einfügen von statischen werten (als string)
# c.execute("INSERT INTO person(name, telefon) VALUES ('Heinz', '04546546546');")
# con.commit()
# c.close()
# con.close()

names = ['Lisa', 'Elfriede', 'Jörg']
tels = ['54321', '56464564', '89784321']

# # einfügen von variablen
# con = sqlite3.connect('first.db')
# c = con.cursor()
#
# for i in range(len(names)):
#     c.execute("INSERT INTO person(name, telefon) VALUES (?, ?);",
#          (names[i], tels[i]))
# con.commit()
# c.close()
# con.close()

# # einfügen mit hilfe des 'with' operators
# with sqlite3.connect('first.db') as con:
#     c = con.cursor()
#     c.execute("INSERT INTO person(name, telefon) VALUES (?, ?);",
#               ('Gerda', '85464'))
#     con.commit()
#     c.close()

############## READ ######################

# alles auswählen in tabelle 'person'
con = sqlite3.connect('first.db')
c = con.cursor()
c.execute("SELECT * FROM person")

for line in c:
    print(line)

# # cursor 'c' ist nach der ausgabe leer
print("########")
# for line in c:
#     print(line)

c.close()
con.close()


n = 'Gerda'
# ausgabe von eintrag mit name == 'Gerda'
con = sqlite3.connect('first.db')
c = con.cursor()

c.execute("SELECT name, telefon FROM person WHERE name = ?",
         [n])

# # bei übergabe von nur einer variable muß das tupel (x, ) sein
# c.execute("SELECT name, telefon FROM person WHERE name = ?",
#          (n, ))

for line in c:
    print(line)

c.close()
con.close()

################### UPDATE ##################

n = 'Gerda'
new_tel = '11115454'
n2 = 'Heinz'


con = sqlite3.connect('first.db')
c = con.cursor()

c.execute("""UPDATE person SET telefon = ?
             WHERE name = ? OR name = ?;""", (new_tel, n, n2))

con.commit()
c.close()
con.close()


################## DELETE ###################
n = 'Lisa'
con = sqlite3.connect('first.db')
c = con.cursor()


c.execute('DELETE FROM person WHERE name = ?;', [n])
# c.execute('DELETE FROM person WHERE name = ?;', (n, ))
con.commit()
c.close()
con.close()
