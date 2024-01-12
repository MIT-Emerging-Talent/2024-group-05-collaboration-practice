# Product of two arrays
# Given two arrays of integers, return an array of the products of the two arrays.


def array_product(arr1, arr2):
    
    arr3 = []
    for i in range(len(arr1)):
        arr3.append(arr1[i] * arr2[i])
    return arr3

if __name__ == "__main__":
    print(array_product([1, 2, 3], [4, 5, 6]))
    # [30, 24, 20]
    print(array_product([1, 2, 3], [4, 5, 6]))
    # [30, 24, 20]
    print(array_product([1, 2, 3], [4, 5, 6]))
    # [30, 24, 20]