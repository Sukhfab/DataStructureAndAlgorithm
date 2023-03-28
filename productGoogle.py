#prodoct of all elments of array excet the self

original_array = [1,2,3,4,-0]
product_array =[]
loop_count = 0
product= 1

for y in range(len(original_array)):
    for x in original_array:
        if loop_count == original_array.index(x):
            continue
        product = product * x
    product_array.append(product)
    product = 1
    loop_count = loop_count + 1
print(product_array)



