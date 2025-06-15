import random
from functools import reduce

def multiply_numbers(num_list):
    attempts = 0
    while attempts < 3:
        product = reduce(lambda x, y: x * y, num_list)
        if product % 2 == 0:
            print(f"Product is even: {product}")
            return product
        random_num = random.randint(1, 1000)
        num_list.append(random_num)
        print(f"Product is odd: {product}, appending {random_num} to the list -> {num_list}")
        attempts += 1
    product = reduce(lambda x, y: x * y, num_list)
    print(f"Final Product after {attempts} attempts: {product}")
    return product
 