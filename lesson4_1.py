some_list = [1,2,3,4,5,6]
if len(some_list) == 0:
    print(0)
x = sum(some_list[2] for _ in range(0, len(some_list),2))
result = x * some_list[-1]
print(result)