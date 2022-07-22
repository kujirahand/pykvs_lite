import pykvs_lite as kvs

# set table_name
kvs.connect()
kvs.set('hoge', 123)
print(kvs.get('hoge'))


