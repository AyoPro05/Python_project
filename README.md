# Arithmetic Arranger

This Python function, `arithmetic_arranger`, takes a list of arithmetic problems as strings and arranges them vertically, as if they were written on an arithmetic worksheet. It supports addition and subtraction only and handles basic error checking.

## Usage

```python
def arithmetic_arranger(problems, show_answers=False):
    # ... (function code as provided) ...

    The function takes two arguments:

problems: A list of strings representing the arithmetic problems. Each problem should be in the format "operand1 operator operand2", where operand1 and operand2 are integers and operator is either "+" or "-".
show_answers (optional): A boolean value. If True, the function will also display the answers to the problems. Defaults to False.

Example Usage

print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
# Output:
#   3801      123
# -    2    +  49
# ------    -----

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
# Output:
#     32      3801      45      123
# +  698    -    2    +  43    +  49
# -----    ------    ----    -----
#   730      3799      88      172



Error Handling

The function includes error handling for the following cases:

Too many problems: If the input list problems contains more than 5 problems, the function returns the string 'Error: Too many problems.'.

Invalid operator: If a problem contains an operator other than "+" or "-", the function returns the string "Error: Operator must be '+' or '-'.".

Non-digit operands: If an operand in a problem is not a valid integer (contains non-digit characters), the function returns the string 'Error: Numbers must only contain digits.'.

Operands with more than four digits: If an operand in a problem has more than four digits, the function returns the string 'Error: Numbers cannot be more than four digits.'.
Function Details

The function works by:

Parsing the problems: It splits each problem string into its operands and operator.
Validating the input: It checks for the errors mentioned above.
Calculating the answers: It calculates the result of each operation.
Arranging the problems: It formats the problems vertically, aligning the operands and adding dashes.
Returning the formatted string: It returns the arranged problems as a single string, with newlines separating the rows.

Testing

The code includes several example calls to arithmetic_arranger with different inputs to demonstrate its functionality and error handling. You can uncomment these calls to test the function yourself.

## Note

Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements of this project, please open an issue or submit a pull 1  request. 

Thank you! 
