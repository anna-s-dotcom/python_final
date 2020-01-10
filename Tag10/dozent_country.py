import sqlite3

class Country_DB:
    def __init__(self, name):
        self.filename = name + '.db'
        self.__createDB()

    def __createDB(self):
        with sqlite3.connect(self.filename) as con:
            con.execute("PRAGMA foreign_keys = ON")
            c = con.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS countries(name TEXT PRIMARY KEY, population INTEGER, capital TEXT );""")

            c.execute("""CREATE TABLE IF NOT EXISTS
                    cities(id INTEGER PRIMARY KEY,
                            name TEXT, country TEXT,
                            capital INTEGER,
                            FOREIGN KEY (country)
                            REFERENCES countries(name));""")
            c.close()

    def insert_country(self, name, pop, cap):
        with sqlite3.connect(self.filename) as con:
            con.execute("PRAGMA foreign_keys = ON")
            c = con.cursor()
            try:
                c.execute("""INSERT INTO countries(name, population, capital) VALUES (?, ?, ?);""", (name, pop, cap))
            except:
                pass

            con.commit()
            c.close()


    def insert_city(self, name, country, cap):
        with sqlite3.connect(self.filename) as con:
            con.execute("PRAGMA foreign_keys = ON")
            c = con.cursor()
            try:
                c.execute("""INSERT INTO cities(name, country,
                capital) VALUES (?, ?, ?);""", (name, country, cap))
            except:
                pass

            con.commit()
            c.close()

    # c ist cursor -> liste = c.fetchall()
    def selectAll(self, table):
        with sqlite3.connect(self.filename) as con:
            con.execute("PRAGMA foreign_keys = ON")
            c = con.cursor()
            if table == 'countries':
                c.execute('SELECT * FROM countries')
            elif table == 'cities':
                c.execute('SELECT * FROM cities')

            # # möglichkeit ohne if
            # try:
            #     c.execute(f'SELECT * FROM {table}')
            #     c.execute(f'SELECT * FROM ' + table)
            # except:
            #     pass

            entries = c.fetchall()
            c.close()
        return entries

    def selectCountry(self, country):
        with sqlite3.connect(self.filename) as con:
            con.execute("PRAGMA foreign_keys = ON")
            c = con.cursor()

            c.execute("SELECT * FROM countries WHERE name = ?;",
                        [country])
            country = c.fetchone()

            c.close()
        return country

    def wrongCities(self):
        with sqlite3.connect(self.filename) as con:
            con.execute("PRAGMA foreign_keys = ON")
            c = con.cursor()
            c.execute('SELECT capital FROM countries;')
            correct = c.fetchall()

            c.execute('SELECT name FROM cities WHERE capital = 1;')
            maybe_correct = c.fetchall()
            c.close()
        # print(correct)
        # print(maybe_correct)
        not_correct = []
        for elem in maybe_correct:
            if elem not in correct:
                not_correct.append(elem)
        # print(not_correct)
        return not_correct

    def cleanup(self):
        with sqlite3.connect(self.filename) as con:
            con.execute("PRAGMA foreign_keys = ON")
            c = con.cursor()

            wrongs = self.wrongCities()
            if len(wrongs) > 0:
                for elem in wrongs:
                    c.execute('UPDATE cities SET capital = 0 WHERE name = ?', elem)
                con.commit()
            c.close()

my_db = Country_DB('country')

# erstelle 'insert_country' methode
name = 'Germany'
pop = 83
hauptstadt = 'München'

# my_db.insert_country(name, pop, hauptstadt)
# my_db.insert_city(hauptstadt, name, 1)

# countries = my_db.selectAll('countries')
# # countries ist eine Liste von Tupeln
# print(countries)
# country = my_db.selectCountry('Germasdany')
# print(country)

my_db.cleanup()
