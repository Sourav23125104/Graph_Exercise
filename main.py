from add import add_numbers
from multiply import multiply_numbers
from divide import divide_first_last

def get_integer_list():
    print("Enter at least 2 integers one by one (type 'done' to finish):")
    print("Note: The last integer entered cannot be 0.")

    while True:
        num_list = []
        while True:
            user_input = input("> ")
            if user_input.lower() == 'done':
                break
            try:
                num = int(user_input)
                num_list.append(num)
            except ValueError:
                print("Invalid input. Please enter an integer or 'done'.")

        if len(num_list) < 2:
            print("Error: You must enter at least 2 integers.")
            continue

        if num_list[-1] == 0:
            print("Invalid input: The last integer cannot be 0. Please re-enter the numbers.")
            continue

        return num_list

if __name__ == "__main__":
    numbers = get_integer_list()
    print(f"Initial List: {numbers}")

    add_numbers(numbers)
    multiply_numbers(numbers)
    divide_first_last(numbers)
