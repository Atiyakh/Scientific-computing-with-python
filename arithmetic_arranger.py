def arithmetic_arranger(problems, solve=False):
    lnumAlign = lambda text, n: ((" " * (n - len(text))) + text)
    rnumAlign = lambda text, n, o: (o + (" " * (n - len(text) -1)) + text)
    if solve: height = 4
    else: height = 3
    structure = {}
    for i in range(height): structure[i] = []
    if len(problems) > 5: return "Error: Too many problems."
    else:
        result = ''
        for problem in problems:
            if '-' in problem or '+' in problem:
                if problem.count('-'): op = '-'
                else: op = '+'
                lnum, rnum = problem.split(f' {op} ')
                try:
                    int(rnum); int(lnum)
                    width =  max([len(rnum), len(lnum)]) + 2
                    if max([len(rnum), len(lnum)]) >= 5:
                        return "Error: Numbers cannot be more than four digits."
                    if solve: data = [lnumAlign(lnum, width), rnumAlign(rnum, width, op), '-' * width, lnumAlign(str(eval(problem)), width)]
                    else: data = [lnumAlign(lnum, width), rnumAlign(rnum, width, op), '-' * width]
                    for key in structure:
                        structure[key] = structure[key] + [data[key]]
                except:
                    return 'Error: Numbers must only contain digits.'
            else:
                return "Error: Operator must be '+' or '-'."
        for i in structure.values():
            result += ('    '.join(i)+'\n')
        return result[:-1]
