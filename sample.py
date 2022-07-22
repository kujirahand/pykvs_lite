import pykvs_lite as kvs
import json

kvs.connect()
kvs.set('hoge', 1234)
kvs.set('fuga', 'いろは')
kvs.set('foo', [1,2,3])

# get
print(kvs.get('fuga'))

print(kvs.keys())
kvs.delete('fuga')
print(kvs.keys())

# enums
for key in kvs.keys():
    print(key, '=', json.dumps(kvs.get(key), ensure_ascii=False))

# get_info
print('info=', kvs.get_info('hoge'))

print(kvs.dump_json())
kvs.close()
