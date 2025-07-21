def arithmetic_arranger(problems, show_answers=False):
    if len(problems)>5:
        return 'Error: Too many problems.'
    first_line=[]
    second_line=[]
    dashes=[]
    answers=[]
    for problem in problems:
      left,op,right=problem.split()
      if op=='*' or op=='/':
          return "Error: Operator must be '+' or '-'."
      if not left.isdigit() or not right.isdigit():
          return "Error: Numbers must only contain digits."
      if len(left)>4 or len(right)>4:
          return"Error: Numbers cannot be more than four digits."
      width=max(len(left),len(right))+2
      first_line.append(left.rjust(width))
      second_line.append(op+right.rjust(width-1))
      dashes.append('-'*width)
      if show_answers:
          result=str(eval(left+op+right))
          answers.append(result.rjust(width))
    arranged_problems="    ".join(first_line)+"\n"+\
                      "    ".join(second_line)+"\n"+\
                      "    ".join(dashes)
    if show_answers:
        arranged_problems+="\n"+"    ".join(answers)         
    return arranged_problems

print(f'{arithmetic_arranger(["4 + 855", "988 + 40"], True)}')
