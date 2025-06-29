import sys
import os


class Stack():
    def __init__(self):
        self.stack = []
    
    def Push(self, value: int):
        self.stack.append(value)
    
    def Pop(self):
        top = str(self.Top())
        self.stack.remove(top)
        return top
    
    def Add(self):
        values = (self.Pop(), self.Pop())
        return (int(values[0]) + int(values[1]))
    
    def Sub(self):
        values = (self.Pop(), self.Pop())
        return (int(values[0]) - int(values[1]))

    def Top(self):
        return int(self.stack[len(self.stack) - 1])


class Function():
    def __init__(self, name: str, commands: list):
        self.name = name
        self.commands = commands


def Execute(toExecute: list):
    for i in toExecute:
        commandParts = i.split(" ")

        if commandParts[0] == "PUSH":
            stack.Push(commandParts[1])
        elif commandParts[0] == "POP":
            value = stack.Pop()
            print(value)
        elif commandParts[0] == "ADD":
            value = stack.Add()
            stack.stack.append(value)
        elif commandParts[0] == "SUB":
            value = stack.Sub()
            stack.stack.append(value)
        elif commandParts[0] == "PRINT":
            value = commandParts[1]
            print(value)
        elif commandParts[0] == "READ":
            value = input(str(commandParts[1]))
            stack.Push(value)
        elif commandParts[0] == "JUMP.EQ.0":
            value = stack.Top()
            if value == 0:
                for e in functions:
                    if e.name == commandParts[1]:
                        Execute(e.commands)
        elif commandParts[0] == "JUMP.GT.0":
            value = stack.Top()
            if value > 0:
                for e in functions:
                    if e.name == commandParts[1]:
                        Execute(e.commands)
        elif commandParts[0] == "HALT":
            sys.exit()


stack = Stack()
functionStart = "FUNC"
functionEnd = "/"

filePath = input("File Path: ")
if os.path.exists(filePath) and os.path.isfile(filePath):
    with open(filePath) as file:
        commands = []
        for i in file:
            commands.append(i.rstrip("\n"))

        functions = []
        for i in commands:
            commandParts = i.split(" ")
            if commandParts[0] == functionStart:
                start = commands.index(i)
                lines = []
                line = start + 1
                while not commands[line] == functionEnd:
                    if not commands[line] == "":
                        lines.append(commands[line])
                    line += 1
                
                function = Function(commandParts[1], lines)
                functions.append(function)

                for e in range(line - start + 1):
                    commands.remove(commands[start])

        Execute(commands)
