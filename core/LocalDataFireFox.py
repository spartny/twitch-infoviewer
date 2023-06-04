import sqlite3
from os import path
import os

# "C:\Users\parth\AppData\Roaming\Mozilla\\Firefox\\Profiles\\pu0zefqs.default-release\\storage\\default\\https+++www.twitch.tv\\ls\\data.sqlite"


profilePath = path.expandvars(r'%APPDATA%\\Mozilla\\Firefox\\Profiles')

profiles = os.listdir(profilePath)

profileName = ''

for profile in profiles:
    if '.default-release' in profile:
        profileName = profile

dataPath = path.expandvars(
    r'%APPDATA%\\Mozilla\\\\Firefox\\Profiles\\' + profileName + '\\storage\\default\\https+++www.twitch.tv\\ls\\data.sqlite')

cachePath = path.expandvars(
    r'%APPDATA%\\Mozilla\\\\Firefox\\Profiles\\' + profileName + '\\storage\\default\\https+++www.twitch.tv\\cache\\caches.sqlite')

idb = path.expandvars(
    r'%APPDATA%\\Mozilla\\\\Firefox\\Profiles\\' + profileName + '\\storage\\default\\https+++www.twitch.tv\\idb\\3966727148sswnnooittiafci.sqlite')


def extraction(choice):
    if choice == "Data":
        con = sqlite3.connect(dataPath)
        cur = con.cursor()
        result = ""
        for row in cur.execute('SELECT * FROM data;'):
            result += str(row) + '\n'
        print(result)
        con.close()
        return result

    elif choice == "Cache":
        con = sqlite3.connect(cachePath)
        cur = con.cursor()
        result = ""
        for row in cur.execute('SELECT * FROM caches;'):
            result += str(row) + '\n'
        print(result)
        con.close()
        return result

    elif choice == "IDB":
        con = sqlite3.connect(idb)
        cur = con.cursor()
        result = ""
        for row in cur.execute('SELECT * FROM object_store_index;'):
            result += str(row) + '\n'
        print(result)
        con.close()
        return result
