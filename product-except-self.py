def product_except_self(array: list[int])-> list[int]:
    left = 1
    right = 1
    product= []
    
    for value in array:
        product.append(left)
        left = left * value
    
    
    for i in range(len(array) -1, -1, -1):
        product[i] = product[i] * right
        right = right * array[i]
    
    return product


if __name__ == "__main__":
    result = product_except_self([1, 1, 2, 0])
    print(result)