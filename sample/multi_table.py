import pykvs_lite as kvs

# set table_name
kvs.connect(table_name='no1')
kvs.set('hoge', 123)

# change table_name
kvs.connect(table_name='no2')
print(kvs.get('hoge', 'not_exists')) # show 'not_exists'

