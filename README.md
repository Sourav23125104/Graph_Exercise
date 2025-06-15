# Graph Exercise

## Overview
This is a modular Python project that performs arithmetic operations (Addition, Multiplication, Division) on user-provided integers with specific validation rules and logic.

## Project Structure

```
├── main.py         # Takes input and controls the flow
├── add.py          # Contains the add_numbers() function
├── multiply.py     # Contains the multiply_numbers() function
└── divide.py       # Contains the divide_first_last() function
```

## Branches Created
1. **dev/satyajeet** 
   - Created: `divide.py`, `multiply.py`
   
2. **dev/sourav** 
   - Created: `main.py`, `add.py`

## Features & Conditions

### Input Conditions:
- Users must enter **at least 2 integers**.
- The **last entered integer cannot be 0**.
- If invalid input → prompt the user to enter again.

### `add_numbers()` (add.py)
- Adds all integers from the list.
- If the sum is **odd**, appends a **random integer (1 to 1000)** to the list.
- Repeats **up to 3 times** or until the sum becomes **even**.

### `multiply_numbers()` (multiply.py)
- Multiplies all integers from the list.
- If the product is **odd**, appends a **random integer (1 to 1000)** to the list.
- Repeats **up to 3 times** or until the product becomes **even**.

### `divide_first_last()` (divide.py)
- Divides **first element / last element** of the list.
- If result < 0.5 → **floor** value is used.
- Else → **ceil** value is used.

## How to Run
```bash
python main.py


