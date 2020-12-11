# https://leetcode.com/problems/goal-parser-interpretation/


def interpret(command):
    result = ""
    for i in range(len(command)):
        if command[i] == "G":
            result += command[i]
        elif command[i] == "(":
            if command[i+1] == ")":
                result += "o"
            else:
                result += "al"
        elif command[i] == ")" or command[i] == "a" or command[i] == "l":
            continue
    return result


def interpret1(command):
    command = command.replace("()","o")
    command = command.replace("(al)", "al")
    return command


# print(interpret1("(al)G(al)()()G"))