# Задайте последовательность чисел. Напишите программу, которая 
# # выведет список неповторяющихся элементов исходной последовательности

# 1-й вариант:

list_in = list(map(int,input('Enter your space-separated numbers:\n').split()))
list_out = [item for item in list_in if list_in.count(item) == 1]
print('Your list of non-repeating elements:\n', list_out)

# 2-й вариант: 

list_in = list(map(int,input('Enter your space-separated numbers:\n').split()))
list_out = list(filter(lambda x: list_in.count(x) == 1, list_in))
print('Your list of non-repeating elements:\n', list_out)
