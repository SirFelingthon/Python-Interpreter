# Python Interpreter

A simple, stack-based interpreter made with python. When running, copy the file path of the code you want to run into the python terminal.

<ins>**Commands**</ins>:
- **PUSH** <ins>*-number-*</ins>: pushes the -number- into the Stack
- **POP**: removes the top value of the stack and prints into the terminal
- **ADD**: adds the 2 uppest values of the stack, removes them and pushes the outcome to the stack
- **SUB**: subs the 2 uppest values of the stack, removes them and pushes the outcome to the stack
- **PRINT** *-string-*: prints the -string- to the python terminal
- **READ**: reads integer input in the python terminal and pushes it to the stack
- **JUMP.EQ.0** *-name-*: if the top value of the stack is equal to 0, runs the function with the corresponding -name-, else runs the following code
- **JUMP.GT.0** *-name-*: if the top value of the stack is greater than 0, runs the function with the corresponding -name-, else runs the following code
- **HALT**: ends the program

<ins>**Functions**</ins>:
- to make a function, simply write FUNC and the name for the function, below the code lines, and at the end of the function a / sign
