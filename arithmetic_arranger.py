def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    operators, numbers, answers = [], [], []
    first_line, second_line, dashes, answer_row = '', '', '', ''

    # Process problems
    for problem in problems:
        parts = problem.split()
        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not parts[0].isdigit() or not parts[2].isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        operators.append(parts[1])
        numbers.append(parts[0])
        numbers.append(parts[2])

        # Calculate answers
        if parts[1] == '+':
            answers.append(int(parts[0]) + int(parts[2]))
        else:
            answers.append(int(parts[0]) - int(parts[2]))

    # Arrange problems
    for i in range(0, len(numbers), 2):
        space_width = max(len(numbers[i]), len(numbers[i + 1])) + 2
        first_number = numbers[i].rjust(space_width)
        second_number = operators[i // 2] + ' ' + numbers[i + 1].rjust(space_width - 2)

        first_line += first_number + '    '
        second_line += second_number + '    '
        dashes += '-' * space_width + '    '

        if show_answers:
            answer_row += str(answers[i // 2]).rjust(space_width) + '    '

    # Return result
    if show_answers:
        return '\n'.join([first_line.rstrip(), second_line.rstrip(), dashes.rstrip(), answer_row.rstrip()])
    else:
        return '\n'.join([first_line.rstrip(), second_line.rstrip(), dashes.rstrip()])

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["1 + 2", "1 - 9380"])}')
print(f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')
print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}')
print(f'\n{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')