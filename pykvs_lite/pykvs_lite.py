"""
Simple and convenient Key-value Store Library
"""

import sqlite3, time, json

global db, cache_keys, cache_db, sqls, cur_filename
db = None
cache_db = {}
cache_keys = {}
sqls = {}
cur_filename = ':memory:'
# SQL template
sqls_template = {
    'create': '''
    CREATE TABLE IF NOT EXISTS __TABLE_NAME__ (
        key_id INTEGER PRIMARY KEY,
        key TEXT UNIQUE,
        value TEXT DEFAULT '',
        ctime INTEGER DEFAULT 0,
        mtime INTEGER DEFAULT 0
    )
    ''',
    'select': 'SELECT value FROM __TABLE_NAME__ WHERE key=?',
    'select_info': 'SELECT * FROM __TABLE_NAME__ WHERE key=?',
    'keys': 'SELECT key FROM __TABLE_NAME__',
    'insert': 'INSERT INTO __TABLE_NAME__ (key, value, ctime, mtime) VALUES (?, ?, ?, ?)',
    'update': 'UPDATE __TABLE_NAME__ SET value=?, mtime=? WHERE key=?',
    'delete': 'DELETE FROM __TABLE_NAME__ WHERE key=?',
    'clear': 'DELETE FROM __TABLE_NAME__',
}

def connect(filename = ':memory:', table_name='kvs'):
    """Connect to database"""
    global sqls, cache_db, cur_filename
    # generate sqls
    sqls = {}
    for key in sqls_template:
        sqls[key] = sqls_template[key].replace('__TABLE_NAME__', table_name)
    # connect to sqlite3
    global db
    if filename in cache_db: # already open?
        db = cache_db[filename] # use_cache
    else:
        db = sqlite3.connect(filename)
        cache_db[filename] = db
    cur_filename = filename
    try:
        # create table
        cur = db.cursor()
        cur.execute(sqls['create'], [])
        # make cache keys
        kvs_keys(True)
    except Exception as e:
        raise Exception('could not initalize database file: ' + str(e))
    finally:
        cur.close()
    return db

def change_db(filename = ':memory:', table_name = 'kvs'):
    """Change Database"""
    connect(filename, table_name)

def close():
    """close database"""
    global db, cur_filename
    if db is not None:
        del cache_db[cur_filename]
        db.close()
    db = None
    cur_filename = ''

def get(key, default = ''):
    """get data"""
    if db is None: raise Exception('please connect before using `get` method.')
    if key not in cache_keys:
        return default
    try:
        cur = db.cursor()
        cur.execute(sqls['select'], [key])
        v = cur.fetchone()
        return json.loads(v[0])
    except Exception as e:
        raise Exception('could not read database: ' + str(e))
    finally:
        cur.close()

def get_info(key, default = ''):
    """get data and info"""
    if db is None: raise Exception('please connect before using `get` method.')
    if key not in cache_keys:
        return default
    try:
        cur = db.cursor()
        cur.execute(sqls['select_info'], [key])
        v = cur.fetchone()
        return v
    except Exception as e:
        raise Exception('could not read database: ' + str(e))
    finally:
        cur.close()


def set(key, value):
    """set data"""
    if db is None: raise Exception('please connect before using `set` method.')
    try:
        cur = db.cursor()
        if key in cache_keys:
            cur.execute(sqls['update'], [value, int(time.time()), key])
        else:
            cur.execute(sqls['insert'], [key, json.dumps(value, ensure_ascii=False), int(time.time()), int(time.time())])
            cache_keys[key] = True
    except Exception as e:
        raise Exception('could not read database: ' + str(e))
    finally:
        cur.close()

def delete(key):
    """delete key"""
    if db is None: raise Exception('please connect before using `delete` method.')
    try:
        cur = db.cursor()
        if key in cache_keys:
            cur.execute(sqls['delete'], [key])
            del cache_keys[key]
    except Exception as e:
        raise Exception('could not read database: ' + str(e))
    finally:
        cur.close()
        
def kvs_keys(clearCache = True):
    """get keys"""
    global cache_keys
    if db is None: return []
    # Use Cache?
    if clearCache or len(cache_keys) == 0:
        cur = db.cursor()
        cur.execute(sqls['keys'])
        cache_keys = {}
        for i in cur.fetchall():
            cache_keys[i[0]] = True
    return cache_keys.keys()

def dump_json():
    """dump json"""
    obj = {}
    for key in kvs_keys():
        obj[key] = get(key, '')
    return json.dumps(obj, ensure_ascii=False)

def clear():
    """clear all"""
    global cache_keys
    if db is None: raise Exception('please connect before using `clear` method.')
    try:
        cur = db.cursor()
        cur.execute(sqls['clear'])
        cache_keys = {}
    except Exception as e:
        raise Exception('could not read database: ' + str(e))
    finally:
        cur.close()
