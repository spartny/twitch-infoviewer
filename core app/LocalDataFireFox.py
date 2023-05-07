import sqlite3
from os import path
import os

#"C:\Users\parth\AppData\Roaming\Mozilla\\Firefox\\Profiles\\pu0zefqs.default-release\\storage\\default\\https+++www.twitch.tv\\ls\\data.sqlite"


profilePath = path.expandvars(r'%APPDATA%\\Mozilla\\Firefox\\Profiles')

profiles = os.listdir(profilePath)

profileName = ''

for profile in profiles:
    if '.default-release' in profile:
        profileName = profile

dataPath = path.expandvars(r'%APPDATA%\\Mozilla\\\\Firefox\\Profiles\\'+profileName+'\\storage\\default\\https+++www.twitch.tv\\ls\\data.sqlite')

cachePath = path.expandvars(r'%APPDATA%\\Mozilla\\\\Firefox\\Profiles\\pu0zefqs.default-release\\storage\\default\\https+++www.twitch.tv\\cache\\caches.sqlite')



# Create a SQL connection to our SQLite database
con = sqlite3.connect(dataPath)

cur = con.cursor()

# The result of a "cursor.execute" can be iterated over by row
for row in cur.execute('SELECT key FROM data;'):
    print(row)

# Be sure to close the connection
con.close()