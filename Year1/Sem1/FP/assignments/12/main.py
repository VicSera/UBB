"""
Generate all sequences of n parentheses that close correctly. Example: for n=4 there are two
solutions: (()) and ()().
"""
from Backtracking import parantheses_recursive, parantheses_iterative

if __name__ == '__main__':
    n = int(input('--> '))

    print('Recursive:')
    parantheses_recursive(n)
    print('Iterative:')
    parantheses_iterative(n)