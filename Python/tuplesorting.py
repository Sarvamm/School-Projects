#tuple sorting 
my_tuple = (('John', 25), ('Jane', 30), ('Mike', 28))
print('Original Tuple:', my_tuple)
#sorting tuple in different ways
sorted_tuple = sorted(my_tuple, key=lambda x: x[1])
print('Sorted Tuple:', sorted_tuple)

sorted_tuple2 = sorted(my_tuple, key=lambda x: x[0])
print('Sorted Tuple:', sorted_tuple2)




