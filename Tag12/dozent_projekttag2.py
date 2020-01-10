import sqlite3

class BlogsDB:
    def __init__(self, name):
        self.filename = name+'.db'
        self.__createDB()


    def __createDB(self):
        con = sqlite3.connect(self.filename)
        c = con.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS
        users(username TEXT PRIMARY KEY, email TEXT);''')

        c.execute('''CREATE TABLE IF NOT EXISTS
        blogs(id INTEGER  PRIMARY KEY,
        author TEXT,
        content TEXT,
        FOREIGN KEY (author) REFERENCES users(username));''')

        c.close()
        con.close()


# 1)
    def createUser(self, name, email):
        con = sqlite3.connect(self.filename)
        c = con.cursor()

        try:
            c.execute('''INSERT INTO users(username, email)
                         VALUES (?, ?);''', (name, email))
            con.commit()
        except Exception as e:
            print(e)

        c.close()
        con.close()

    def updateUser(self, name, email):
        con = sqlite3.connect(self.filename)
        c = con.cursor()

        c.execute('''UPDATE users SET email = ?
                     WHERE username = ?;''', (email, name))
        con.commit()

        c.close()
        con.close()


    def create_updateUser(self, name, email):
        con = sqlite3.connect(self.filename)
        c = con.cursor()

        try:
            c.execute('''INSERT INTO users(username, email)
                         VALUES (?, ?);''', (name, email))
        except:
            c.execute('''UPDATE users SET email = ?
                         WHERE username = ?;''', (email, name))
        con.commit()

        c.close()
        con.close()


# 2)
    def deleteUser(self, name):
        con = sqlite3.connect(self.filename)
        c = con.cursor()

        c.execute('DELETE FROM blogs WHERE author = ?;',
                 (name, ))
        c.execute('DELETE FROM users WHERE username = ?;',
                 (name, ))
        con.commit()

        c.close()
        con.close()


# 3)
    def createBlog(self, user, content):
        con = sqlite3.connect(self.filename)
        con.execute('PRAGMA foreign_keys = ON')
        c = con.cursor()

        try:
            c.execute('''INSERT INTO blogs(author, content)
                         VALUES (?, ?);''',
                         (user, content))
            con.commit()
        except Exception as e:
            print(e)


    def updateBlog(self, id, content):
        con = sqlite3.connect(self.filename)
        c = con.cursor()

        c.execute('''UPDATE blogs SET content = ?
                     WHERE id = ?;''', (content, id))
        con.commit()

        c.close()
        con.close()

# 4)
    def findBlogs(self, user):
        con = sqlite3.connect(self.filename)
        c = con.cursor()

        c.execute('''SELECT id, content
                     FROM blogs
                     WHERE author = ?;''', (user, ))

        blogs = c.fetchall()

        c.close()
        con.close()

        print('AUTHOR:', user)
        for blog in blogs:
            print('ID:', blog[0])
            print()
            print(blog[1])
            print('##############')


# 5)
    def getUser(self, id):
        con = sqlite3.connect(self.filename)
        c = con.cursor()

        c.execute('SELECT author FROM blogs WHERE id = ?;',
                   (id, ))
        user = c.fetchone()

        c.close()
        con.close()

        try:
            print(user[0])
        except:
            print('Blog ID nicht vergeben.')


if __name__ == '__main__':

    myDB = BlogsDB('blogs')

    # 1)
    myDB.createUser('jp', 'j@p.com')
    myDB.createUser('jp2', 'bla@no.com')

    myDB.updateUser('jp2', 'x@y.com')

    myDB.create_updateUser('jp3', 'a@b.com')
    myDB.create_updateUser('jp3', 'j@pop.com')

    # 2)
    myDB.deleteUser('jp2')

    # 3)
    myDB.createBlog('jp', 'hello1')
    myDB.createBlog('jp', 'hello2')
    myDB.createBlog('jp', 'hello3')
    myDB.createBlog('jp3', 'No hello1')
    myDB.createBlog('jp3', 'No hello2')
    myDB.createBlog('jp3', 'No hello3')

    myDB.createBlog('jp4', 'should not exist')

    myDB.deleteUser('jp3')

    myDB.updateBlog(1, 'Hello World!')

    # 4)
    myDB.findBlogs('jp')
    myDB.findBlogs('jp6')

    # 5)
    myDB.getUser(1)
    myDB.getUser(100000)
