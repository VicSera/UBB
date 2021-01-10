def parantheses_recursive(n, state="", evaluation=0):
    if evaluation < 0:  # too many closed parantheses (can't be fixed)
        return
    if n == 0:
        if evaluation == 0:
            print(state)
        return

    parantheses_recursive(n - 1, state + ')', evaluation - 1)  # do all branches that contain a ) on the next position
    parantheses_recursive(n - 1, state + '(', evaluation + 1)  # do all branches that contain a ( on the next position

def parantheses_iterative(n):
    if n % 2 == 1:
        print('No solutions for odd numbers')
        return
    # since there are n positions with 2 possible parantheses, there are 2 ** n configurations
    for position in range(2 ** n):
        # each configuration is abinary number in the format 0b____
        configuration = bin(position)[2:]  # cut off 0b from the beginning of the string
        # pad with zeroes up to n so that all positions have a value
        configuration = "0" * (n - len(configuration)) + configuration
        # Now each configuration maps to a string of parantheses:
        # 0 -> (
        # 1 -> )
        state = ['(' if bit == '0' else ')' for bit in configuration]

        evaluation = 0
        for paranthesis in state:
            evaluation += 1 if paranthesis == '(' else -1
            if evaluation < 0:
                break
        if evaluation == 0:
            print(*state, sep='')  # print all the parantheses without the default ' ' print separator
