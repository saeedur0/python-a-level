#insertion sort

items = ["saeedur","abdul","nafis","armaan","haris","umar" ]

n = len(items)
for index in range(1,n):
    current = items[index]
    index2 = index
    while index2 > 0 and items[index2 -1 ] > current:
        items[index2] = items[index2 -1]
        index2 = index2 -1
    items[index2] = current
#Output the result
print(items)
