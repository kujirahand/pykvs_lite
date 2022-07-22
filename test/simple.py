import sys, os, json
sys.path.append(os.path.abspath(".."))
import pykvs_lite as kvs

# get and set
kvs.connect()
kvs.set('a', 1234)
assert 1234 == kvs.get('a'), 'get'
kvs.set('b', [1,2,3,4])
assert 4 == len(kvs.get('b')), 'get :: list'

# clear and delete and keys
kvs.clear()
kvs.set('c', 'abc')
kvs.set('d', 'cde')
kvs.delete('d')
assert json.dumps(list(kvs.keys())) == '["c"]', f'keys=%s' % json.dumps(list(kvs.keys()))
kvs.close()

# change table_name
kvs.connect(table_name='no1')
kvs.set('hello', 123)
assert 123 == kvs.get('hello'), 'get table_name=no1'

kvs.connect(table_name='no2')
assert '' == kvs.get('hello', ''), f'get hello=%s table_name=no2' % kvs.get('hello', '')
kvs.close()

# multi database
kvs.connect(':memory:')
kvs.set('hello', 1234)
kvs.connect('test.db')
assert '' == kvs.get('hello', ''), 'multidatabase'
kvs.close()
os.unlink('test.db')
