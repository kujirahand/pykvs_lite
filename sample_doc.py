import pykvs_lite as kvs
import json

kvs.connect()
kvs.insert({'name': 'Taro', 'age': 10})
kvs.insert({'name': 'Ika', 'age': 11})
kvs.insert({'name': 'Poko', 'age': 12})

print("===")
for c in kvs.all():
    print(c)

print("===")
for c in kvs.recent(2):
    print(c)

print("===")
print('id=1', kvs.get_doc_by_id(1))

print("===")
print(json.dumps(kvs.find(lambda v: v['name']=='Ika')))

print("===")
kvs.clear_doc()
a = kvs.all()
print('len=', len(a))

