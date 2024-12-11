# arithmetic_arranger
def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        print("Error: Too many problems.")

    arranged_problems = []
    top_line, bottom_line, separator_line, answer_line = "", "", "", ""

    for problem in problems:
        elements = problem.split()
        num_1, operator, num_2 = elements

        if not (num_1.isnumeric() and num_2.isnumeric()):
            return("Error: Numbers must only contain digits.")
        if operator not in ["+", "-"]:
            return("Error: Operator must be '+' or '-'.")
        
        width = 4
        space = " "
        sline = "----"
        top_line += ' ' + str(num_1).rjust(width, space) + "    "
        bottom_line += operator + str(num_2).rjust(width, space) + "    "
        separator_line += " " + str(sline).rjust(width, space) + "    "
        try:
            len(num_1) < 5
            len(num_2) < 5
        except:
            print("Error: Numbers cannot be more than four digits.")
        if show_answers:
            if operator == '+' :
                result = str(int(num_1) + int(num_2))
            if operator == '-':
                result = str(int(num_1) - int(num_2))
            answer_line += " " + str(result.rjust(width, space)) + "    "

    arranged_problems.append(top_line.rstrip())
    arranged_problems.append(bottom_line.rstrip())
    arranged_problems.append(separator_line.rstrip())

    if show_answers:
        arranged_problems.append(answer_line.rstrip())
        return('\n'.join(arranged_problems))
    

# Example usage:
problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
print(arithmetic_arranger(problems, True))


        


