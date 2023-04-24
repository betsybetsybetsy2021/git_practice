"""This is the LinkedIn Challenge 4.  To write a function that will find all values in a 
mulit-level list"""

example = [[1,2,3], 2, [1,3], [1,2,3]]
index_list = []

print(type(example))
print(type(example[0]))

example.index(2) # This is the python built-in which cannot
# find values in non-flat lists

for i in len(example):
    index_list.append(i)