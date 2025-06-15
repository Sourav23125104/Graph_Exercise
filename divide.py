import math

def divide_first_last(num_list):
    if num_list[-1] == 0:
        print("Cannot divide by zero (last element is 0).")
        return None

    result = num_list[0] / num_list[-1]

    if result < 0.5:
        final_result = math.floor(result)
        print(f"Dividing first and last elements: {num_list[0]} / {num_list[-1]} = {final_result}")
    else:
        final_result = math.ceil(result)
        print(f"Dividing first and last elements: {num_list[0]} / {num_list[-1]} = {final_result}")

    return final_result
 