import itertools

list1=['a','b','c']
list2=['a','b','c']
# y = set()

# for x in itertools.permutations(list1,len(list1)):
#     y.add(zip(x,list2))

for x in itertools.permutations(list1, 2):
    print(x[0])