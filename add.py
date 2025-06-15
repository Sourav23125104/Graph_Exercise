import random

def add_numbers(num_list):
    attempts = 0
    while attempts < 3:
        total = sum(num_list)
        if total % 2 == 0:
            print(f"Sum is even: {total}")
            return total
        random_num = random.randint(1, 1000)
        num_list.append(random_num)
        print(f"Sum is odd: {total}, appending {random_num} to the list -> {num_list}")
        attempts += 1
    total = sum(num_list)
    print(f"Final Sum after {attempts} attempts: {total}")
    return total
