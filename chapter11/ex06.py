asia_set = {'korea', 'china', 'japan', 'korea'}
asia_dict = {'1':'korea', '2':'china', '3':'japan', '4':'korea'}


print(asia_set)
print(type(asia_set))
print(asia_dict)
print(type(asia_dict))


print(set('aaabbbccc'))         # -> 'a', 'c', 'b'
print(set([12,34,56,78]))
print(set(('a','b','c')))
print(set({'boy':'소년', 'girl':'소녀'}))   # -> key만 뽑혀나온다.
print(set())

asia = {'korea', 'china', 'japan', 'korea'}
asia.add('vietnam')
asia.add('korea')
asia.remove('japan')
print(asia)