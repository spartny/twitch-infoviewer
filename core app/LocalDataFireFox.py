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

cachePath = path.expandvars(r'%APPDATA%\\Mozilla\\\\Firefox\\Profiles\\'+profileName+'\\storage\\default\\https+++www.twitch.tv\\cache\\caches.sqlite')

idb = path.expandvars(r'%APPDATA%\\Mozilla\\\\Firefox\\Profiles\\'+profileName+'\\storage\\default\\https+++www.twitch.tv\\idb\\3966727148sswnnooittiafci.sqlite')



choice = int(input('Select Path (1,2,3) - '))


if choice == 1:
    con = sqlite3.connect(dataPath)

    cur = con.cursor()

    for row in cur.execute('SELECT * FROM data;'):
        print(row)

    # Be sure to close the connection
    con.close()

elif choice == 2:
    con = sqlite3.connect(cachePath)

    cur = con.cursor()

    for row in cur.execute('SELECT * FROM caches;'):
        print(row)

    # Be sure to close the connection
    con.close()

elif choice == 3:
    con = sqlite3.connect(idb)

    cur = con.cursor()

    for row in cur.execute('SELECT * FROM object_store_index;'):
        print(row)

    # Be sure to close the connection
    con.close()