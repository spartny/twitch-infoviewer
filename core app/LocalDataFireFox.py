import sqlite3
from os import path

#"C:\Users\parth\AppData\Roaming\Mozilla\\Firefox\\Profiles\\pu0zefqs.default-release\\storage\\default\\https+++www.twitch.tv\\ls\\data.sqlite"

dataPath = path.expandvars(r'%APPDATA%\\Mozilla\\\\Firefox\\Profiles\\pu0zefqs.default-release\\storage\\default\\https+++www.twitch.tv\\ls\\data.sqlite')

# Create a SQL connection to our SQLite database
con = sqlite3.connect(dataPath)

cur = con.cursor()

# The result of a "cursor.execute" can be iterated over by row
for row in cur.execute('SELECT key FROM data;'):
    print(row)

# Be sure to close the connection
con.close()