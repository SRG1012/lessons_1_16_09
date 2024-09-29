some_list = [0,12,42,0,1,0]
no_zero_index = 0
for i in range(len(some_list)):
 if some_list[i] != 0:
         some_list[no_zero_index] = some_list[i]
         no_zero_index += 1
for i in range(no_zero_index,len(some_list)):
     some_list[i] = 0
print(some_list)

