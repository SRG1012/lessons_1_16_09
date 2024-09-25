some_list123 = [3,6,9,12]
last = len(some_list123)-1
tmp = some_list123[last]
new_list=[tmp] + some_list123[:last]
print(new_list)
