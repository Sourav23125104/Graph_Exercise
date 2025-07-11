import importlib
import pkgutil
import sys
import os

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

def all_operations(numbers):
    current_dir = os.path.dirname(__file__)
    sys.path.insert(0, current_dir)

    known_order = ['add', 'multiply', 'divide']

    for module_name in known_order:
        try:
            module = importlib.import_module(module_name)
            if hasattr(module, 'fn'):
                print(f"\n Running: {module_name}.py ")
                module.fn(numbers)
        except ModuleNotFoundError:
            print(f"Warning: Module '{module_name}' not found.")

    already_run = set(known_order + ['main', '__init__'])

    for _, module_name, _ in sorted(pkgutil.iter_modules([current_dir])):
        if module_name not in already_run:
            module = importlib.import_module(module_name)
            if hasattr(module, 'fn'):
                print(f"\n Running: {module_name}.py ")
                module.fn(numbers)

if __name__ == "__main__":
    nums = get_integer_list()
    print(f"\nInitial List: {nums}")
    all_operations(nums)
