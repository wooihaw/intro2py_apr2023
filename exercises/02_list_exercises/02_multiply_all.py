# Write a Python script to multiply all the items in a list.
alist = [12, 43, 57, 98, 83, -103, 256, -1]
print(f'{alist=}')

prod_list = 1
for i in alist:
    prod_list *= i
print(f"The product is {prod_list}")