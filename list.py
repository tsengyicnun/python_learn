"""
Operation 2
"""

my_list = []
my_list.append(1)
my_list.append(2)


my_list2 = [55.5,"ABC",2,5,222,222,222,333,333]
my_list2[0] = 33.33


print len(my_list),sum(my_list)
print my_list2.count(222),my_list2.count(333)
print my_list2[-2],my_list2[-3]
print my_list2[1:4],my_list2[3:]