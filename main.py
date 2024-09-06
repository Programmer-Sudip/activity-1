lst = ['Apple ', 'Orange ', 'Banana ', 'Mango','Kiwi']

print("Length of lst list is: ", len(lst))
print("First element :", lst[0])
print("Last element :", lst[-1])

lst.append('Papaya')
print("Updated append: ", lst)

lst.remove('Kiwi')
print("Updated remove: ", lst)

lst.sort()
print("Sorted list: ", lst)

lst.pop()
print("Updated pop: ", lst)

lst.reverse()
print("Updated reverse: ", lst)

print("Multiplication on list :", lst*2)

lst = lst[:4]
print("Sliced list: ", lst)

lst.clear()
print("Updated clear: ", lst)