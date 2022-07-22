# pykvs_lite

Key-Value Store for Python

## Features

- Simple and convenient Key-value Store Library
- Easy to install (Use SQLite for the back end)

## Installation

```
$ python3 -m pip install pykvs_lite
```

## Repository

- [GitHub](https://github.com/kujirahand/pykvs_lite)


## Sample

The pykvs has set and get method.
However, you need to connect to the file before you use it.

```simple.py
import pykvs_lite as kvs

# connect to KVS
kvs.connect('test.db')

# set
kvs.set('hoge', 1234)

# get
print(kvs.get('hoge'))

# close
kvs.close()
```

## Sample

```sample2.py
import pykvs_lite as kvs
import json

# connect and set
kvs.connect('test.db')
kvs.set('hoge', 1234)
kvs.set('fuga', 'いろは')
kvs.set('foo', [1,2,3])

# enums
for key in kvs.keys():
    print(key, '=', json.dumps(kvs.get(key), ensure_ascii=False))

# dump to json
print(kvs.dump_json())
kvs.close()
```
