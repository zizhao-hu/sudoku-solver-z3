from z3 import *
import sys
import numpy as np


s = Solver()

#board and number rules
board = [[Int(f'{i},{j}') for j in range(9)] for i in range(9)]

for i in range(9):
    for j in range(9):
        
        s.add(And(1 <= board[i][j], board[i][j] <= 9))
 
for i in range(9):
    s.add(Distinct(board[i])) # row rule
    s.add(Distinct([board[j][i] for j in range(9)])) # col rule
    j = i//3
    k = i%3
    s.add(Distinct([board[j*3+l][k*3+m] for l in range(3) for m in range(3)])) # cell rule

row = 0

print("what's the problem?")
for line in sys.stdin:
    if 'e' == line.rstrip():
        break
    line = line.rstrip()
    for col, char in enumerate(line):
        if char == ' ':
            continue
        else:
            s.add(board[row][col] == int(char))

    row = row + 1
    if row == 9:
        break

if s.check() == sat:
    print("solution:")
    model = s.model()
    eval = [[str(model.evaluate(board[i][j])) for j in range(9)] for i in range(9)]
    for row in eval:
        print(''.join(row))
else: 
    print(unsat)