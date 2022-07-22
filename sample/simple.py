import pykvs_lite as kvs

# connect to KVS
kvs.connect('test.db')

# set
kvs.set('hoge', 1234)

# get
print(kvs.get('hoge'))

# close
kvs.close()

