from add import add_numbers
from multiply import multiply_numbers
from divide import divide_first_last

def get_integer_list():
    print("You need to enter at least 2 integers.")
    print("Note: The last integer must not be 0.")
    while True:
        try:
            count = int(input("How many integers do you want to enter? > "))
            if count < 2:
                print("Please enter at least 2 integers.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        num_list = []
        for i in range(count):
            while True:
                try:
                    num = int(input(f"Enter integer #{i + 1}: "))
                    num_list.append(num)
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
        if num_list[-1] == 0:
            print("The last integer cannot be 0. Please start over.\n")
            continue
        return num_list
if __name__ == "__main__":
    numbers = get_integer_list()
    print(f"Initial List: {numbers}")
    add_numbers(numbers)
    multiply_numbers(numbers)
    divide_first_last(numbers)
