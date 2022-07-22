import pykvs.__init__ as kvs
import json

kvs.connect('test.db')
kvs.set('hoge', 1234)
kvs.set('fuga', 'いろは')
kvs.set('foo', [1,2,3])

# get
print(kvs.get('fuga'))

# enums
for key in kvs.keys():
    print(key, '=', json.dumps(kvs.get(key), ensure_ascii=False))

print(kvs.dump_json())
kvs.close()
