import random
random_list = [random.randint(1, 10) for _ in range(random.randint(3, 10))]
new_list = [random_list[0], random_list[2], random_list[-2]]
print(random_list)
print(new_list)