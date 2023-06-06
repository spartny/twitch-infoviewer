import plyvel

from os import path
import os

import sys
import pathlib
import ccl_chromium_localstorage

ldbPath = path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\Default\Local Storage\\leveldb\\')


level_db_in_dir = pathlib.Path(ldbPath)

# Create the LocalStoreDb object which is used to access the data
with ccl_chromium_localstorage.LocalStoreDb(level_db_in_dir) as local_storage:
    for storage_key in local_storage.iter_storage_keys():
        if storage_key == 'https://www.twitch.tv':
            print(f"Getting records for {storage_key}")

            for record in local_storage.iter_records_for_storage_key(storage_key):
                # we can attempt to associate this record with a batch, which may
                # provide an approximate timestamp (withing 5-60 seconds) for this
                # record.
                batch = local_storage.find_batch(record.leveldb_seq_number)
                timestamp = batch.timestamp if batch else None
                print(record.leveldb_seq_number, record.script_key, record.value, sep="\t")


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







