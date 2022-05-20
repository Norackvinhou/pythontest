
info={'name':'norack', 'age':'20','DP':'CS'}
print(info['age'])

print(list(info))
print(list(info.keys()))
print(list(info.values()))
print(list(info.items()))

for i in info.values():
    print(i)

for i in info.keys():
    print(i)

for i, j in info.items():
    print(i,j)

print(info.get('name', 0))
print(info.get('names', 0))

info.setdefault('id','007')
print(info)

