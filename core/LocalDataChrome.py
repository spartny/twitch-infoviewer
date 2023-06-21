from os import path

import pathlib
import ccl_chrome_indexeddb_master.ccl_chromium_localstorage as cls
import ccl_chrome_indexeddb_master.ccl_chromium_indexeddb as cid
import ccl_chrome_indexeddb_master.ccl_chromium_sessionstorage as css

localStorage_ldbPath = path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\Default\Local Storage\\leveldb\\')

sessionStorage_ldbPath = path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\Default\Session Storage\\')

indexedDb_ldbPath = path.expandvars(r'Users\parth\AppData\Local\Google\Chrome\User Data\Default\IndexedDB\https_www.twitch.tv_0.indexeddb.leveldb')

localStroage_level_db_in_dir = pathlib.Path(localStorage_ldbPath)

sessionStroage_level_db_in_dir = pathlib.Path(sessionStorage_ldbPath)

indexedDb_level_db_in_dir = pathlib.Path(indexedDb_ldbPath)


ifextracted = False

def extraction(choice):
    result = ''
    # Create the LocalStoreDb object which is used to access the data
    if choice == 'www.twitch.tv':
        if ifextracted is True:
            return result
        else:
            with cls.LocalStoreDb(localStroage_level_db_in_dir) as local_storage:
                for storage_key in local_storage.iter_storage_keys():
                    if storage_key == 'https://www.twitch.tv':
                        print(f"Getting records for {storage_key}")
                        for record in local_storage.iter_records_for_storage_key(storage_key):
                            # we can attempt to associate this record with a batch, which may
                            # provide an approximate timestamp (withing 5-60 seconds) for this
                            # record.
                            batch = local_storage.find_batch(record.leveldb_seq_number)
                            timestamp = batch.timestamp if batch else None
                            result += str(record.leveldb_seq_number) + ', ' + str(record.script_key) + ', ' + str(
                                record.value) + '\n'
                            print('\n', record.leveldb_seq_number, record.script_key, record.value, sep="\t")
                            ifextracted = True
                        return result

    if choice == 'local storage - data':
        result = extraction('www.twitch.tv')
        return result

    if choice == 'gql.twitch.tv':
        with cls.LocalStoreDb(localStroage_level_db_in_dir) as local_storage:
            for storage_key in local_storage.iter_storage_keys():
                if storage_key == 'https://gql.twitch.tv':
                    print(f"Getting records for {storage_key}")
                    for record in local_storage.iter_records_for_storage_key(storage_key):
                        # we can attempt to associate this record with a batch, which may
                        # provide an approximate timestamp (withing 5-60 seconds) for this
                        # record.
                        batch = local_storage.find_batch(record.leveldb_seq_number)
                        timestamp = batch.timestamp if batch else None
                        result += str(record.leveldb_seq_number) + ', ' + str(record.script_key) + ', ' + str(
                            record.value) + '\n'
                        print('\n', record.leveldb_seq_number, record.script_key, record.value, sep="\t")

                    return result

    if choice == 'passport.twitch.tv':
        with cls.LocalStoreDb(localStroage_level_db_in_dir) as local_storage:
            for storage_key in local_storage.iter_storage_keys():
                if storage_key == 'https://passport.twitch.tv':
                    print(f"Getting records for {storage_key}")
                    for record in local_storage.iter_records_for_storage_key(storage_key):
                        # we can attempt to associate this record with a batch, which may
                        # provide an approximate timestamp (withing 5-60 seconds) for this
                        # record.
                        batch = local_storage.find_batch(record.leveldb_seq_number)
                        timestamp = batch.timestamp if batch else None
                        result += str(record.leveldb_seq_number) + ', ' + str(record.script_key) + ', ' + str(
                            record.value) + '\n'
                        print('\n', record.leveldb_seq_number, record.script_key, record.value, sep="\t")

                    return result

    if choice == 'Session Storage':
        # Create the SessionStoreDb object which is used to access the data
        with css.SessionStoreDb(sessionStroage_level_db_in_dir) as session_storage: 
            for host in session_storage.iter_hosts():
                if host == 'https://www.twitch.tv/': 
                    print(f"Getting records for {host}")
                    print(host)
                    for key, values in session_storage.get_all_for_host(host).items():
                        for value in values:
                            result += str(value.leveldb_sequence_number) + ', ' + str(value.guid) + ', ' + str(
                                key) + ',' + str(value.value) + '\n'
                            print(value.leveldb_sequence_number, value.guid, key, value.value, sep="\t")
                break
            return result


   


extraction('Session Storage')
# def open_leveldb(db_dir):
#     try:
#         print('test')
#         return plyvel.DB(db_dir, create_if_missing=False)

#     except plyvel._plyvel.IOError as e:
#         raise Exception("Ensure that bitcoind is stopped.")

# # "C:\Users\parth\AppData\Roaming\Mozilla\\Firefox\\Profiles\\pu0zefqs.default-release\\storage\\default\\https+++www.twitch.tv\\ls\\data.sqlite"

# ldbPath = path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\Default\Local Storage\leveldb\\')

# file = open(ldbPath+'test.txt','w')
# file.write("This is a test")
# file.close()

# db1 = plyvel.DB(ldbPath+'004104.ldb', create_if_missing=False)

# print('test')

# print(ldbPath)

# db = plyvel.DB(ldbPath+'\test.db', create_if_missing=True)
