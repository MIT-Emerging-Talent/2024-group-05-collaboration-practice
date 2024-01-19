# Simple solution to the array product problem

def array_product(my_array):
    if len(my_array) == 0:
        return []
    if len(my_array) == 1:
        return my_array
    result = []
    for i in range(len(my_array)):
        product = 1
        for j in range(len(my_array)):
            if i != j:
                product *= my_array[j]
        result.append(product)
    return result

print(array_product([1, 2, 3, 4, 5]))