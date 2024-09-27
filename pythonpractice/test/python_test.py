# HashMap (dictionary)
dct = {}
dct['name'] = 'jason' # put
temp = dct['name'] # get, 없으면 에러
temp2 = dct.get('nam') # get(key, defaultvalue) => 없으면 defaultvalue 리턴
print('name' in dct.keys()) # hashmap에 key가 있는지
print('name' in dct.values()) # hashmap에 value 있는지

print("-" * 100)

# HashSet (set)
st = set()
st.add('asfd') # hashset add
print('asfd' in st) # hashset에 value가 있는지
st.remove('asfd') # hashset remove

print("-" * 100)

# Array (list)
list_1d = []

m, n = 5, 20
list_2d = [[1 for _ in range(n)] for _ in range(m)] # m x n
list_2d = [[1] * n] * m
