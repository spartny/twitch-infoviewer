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
    if choice == "local storage - data":
        con = sqlite3.connect(dataPath)
        cur = con.cursor()
        result = ""
        for row in cur.execute('SELECT * FROM data;'):
            result += str(row) + '\n'
        print(result)
        con.close()
        return result

    elif choice == "local storage - database":
        con = sqlite3.connect(dataPath)
        cur = con.cursor()
        result = ""
        for row in cur.execute('SELECT * FROM database;'):
            result += str(row) + '\n'
        print(result)
        con.close()
        return result

    elif choice == "cache - caches":
        con = sqlite3.connect(cachePath)
        cur = con.cursor()
        result = ""
        for row in cur.execute('SELECT * FROM caches;'):
            result += str(row) + '\n'
        print(result)
        con.close()
        return result

    elif choice == "cache - entries":
        con = sqlite3.connect(cachePath)
        cur = con.cursor()
        result = ""
        for row in cur.execute('SELECT * FROM entries;'):
            result += str(row) + '\n'
        print(result)
        con.close()
        return result

    elif choice == "cache - request_headers":
        con = sqlite3.connect(cachePath)
        cur = con.cursor()
        result = ""
        for row in cur.execute('SELECT * FROM request_headers;'):
            result += str(row) + '\n'
        print(result)
        con.close()
        return result

    elif choice == "cache - response_headers":
        con = sqlite3.connect(cachePath)
        cur = con.cursor()
        result = ""
        for row in cur.execute('SELECT * FROM response_headers;'):
            result += str(row) + '\n'
        print(result)
        con.close()
        return result

    elif choice == "cache - response_url_list":
        con = sqlite3.connect(cachePath)
        cur = con.cursor()
        result = ""
        for row in cur.execute('SELECT * FROM response_url_list;'):
            result += str(row) + '\n'
        print(result)
        con.close()
        return result

    elif choice == "cache - security_info":
        con = sqlite3.connect(cachePath)
        cur = con.cursor()
        result = ""
        for row in cur.execute('SELECT * FROM security_info;'):
            result += str(row) + '\n'
        print(result)
        con.close()
        return result

    elif choice == "cache - sqlite_sequence":
        con = sqlite3.connect(cachePath)
        cur = con.cursor()
        result = ""
        for row in cur.execute('SELECT * FROM sqlite_sequence;'):
            result += str(row) + '\n'
        print(result)
        con.close()
        return result

    elif choice == "cache - storage":
        con = sqlite3.connect(cachePath)
        cur = con.cursor()
        result = ""
        for row in cur.execute('SELECT * FROM storage;'):
            result += str(row) + '\n'
        print(result)
        con.close()
        return result

    elif choice == "idb - database":
        con = sqlite3.connect(idb)
        cur = con.cursor()
        result = ""
        for row in cur.execute('SELECT * FROM database;'):
            result += str(row) + '\n'
        print(result)
        con.close()
        return result

    elif choice == "idb - file":
        con = sqlite3.connect(idb)
        cur = con.cursor()
        result = ""
        for row in cur.execute('SELECT * FROM file;'):
            result += str(row) + '\n'
        print(result)
        con.close()
        return result

    elif choice == "idb - index_data":
        con = sqlite3.connect(idb)
        cur = con.cursor()
        result = ""
        for row in cur.execute('SELECT * FROM index_data;'):
            result += str(row) + '\n'
        print(result)
        con.close()
        return result

    elif choice == "idb - object_data":
        con = sqlite3.connect(idb)
        cur = con.cursor()
        result = ""
        for row in cur.execute('SELECT * FROM object_data;'):
            result += str(row) + '\n'
        print(result)
        con.close()
        return result

    elif choice == "idb - object_store":
        con = sqlite3.connect(idb)
        cur = con.cursor()
        result = ""
        for row in cur.execute('SELECT * FROM object_store;'):
            result += str(row) + '\n'
        print(result)
        con.close()
        return result

    elif choice == "idb - object_store_index":
        con = sqlite3.connect(idb)
        cur = con.cursor()
        result = ""
        for row in cur.execute('SELECT * FROM object_store_index;'):
            result += str(row) + '\n'
        print(result)
        con.close()
        return result

