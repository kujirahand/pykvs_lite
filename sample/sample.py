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


