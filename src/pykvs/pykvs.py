import sqlite3, time, json

global db
global cache_keys
db = None
cache_keys = {}

# create
sql_create = '''
    CREATE TABLE IF NOT EXISTS kvs(
        key_id INTEGER PRIMARY KEY,
        key TEXT UNIQUE,
        value TEXT DEFAULT '',
        ctime INTEGER DEFAULT 0,
        mtime INTEGER DEFAULT 0
    );
'''
# select
sql_get = '''
    SELECT value FROM kvs WHERE key=?
'''
sql_get_keys = '''
    SELECT key FROM kvs;
'''
# insert
sql_insert = '''
    INSERT INTO kvs (key, value, ctime, mtime) VALUES (?, ?, ?, ?)
'''
# update
sql_update = '''
    UPDATE kvs SET value=?, mtime=? WHERE key=?
'''
# delete
sql_delete = '''
    DELETE FROM kvs WHERE key=?
'''

def connect(filename):
    global db
    db = sqlite3.connect(filename)
    try:
        # create table
        cur = db.cursor()
        cur.execute(sql_create, [])
        # make cache keys
        kvs_keys(True)
    except Exception as e:
        raise Exception('could not initalize database file: ' + str(e))
    finally:
        cur.close()
    return db

def close():
    if db is not None:
        db.close()

def get(key, default = ''):
    if db is None: raise Exception('please connect before using `get` method.')
    if key not in cache_keys:
        return default
    try:
        cur = db.cursor()
        cur.execute(sql_get, [key])
        v = cur.fetchone()
        return json.loads(v[0])
    except Exception as e:
        raise Exception('could not read database: ' + str(e))
    finally:
        cur.close()

def set(key, value):
    if db is None: raise Exception('please connect before using `set` method.')
    try:
        cur = db.cursor()
        if key in cache_keys:
            cur.execute(sql_update, [value, int(time.time()), key])
        else:
            cur.execute(sql_insert, [key, json.dumps(value, ensure_ascii=False), int(time.time()), int(time.time())])
            cache_keys[key] = True
    except Exception as e:
        raise Exception('could not read database: ' + str(e))
    finally:
        cur.close()

def kvs_keys(clearCache = True):
    global cache_keys
    if db is None: return []
    # Use Cache?
    if clearCache or len(cache_keys) == 0:
        cur = db.cursor()
        cur.execute(sql_get_keys)
        cache_keys = {}
        for i in cur.fetchall():
            cache_keys[i[0]] = True
    return cache_keys.keys()

def dump_json():
    obj = {}
    for key in kvs_keys():
        obj[key] = get(key, '')
    return json.dumps(obj, ensure_ascii=False)
