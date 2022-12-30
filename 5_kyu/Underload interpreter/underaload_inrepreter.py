# Underload is an esoteric programming language. It is a stack based, turing complete language that works based on strings. Strings are the only datatype in Underload.
#
# Commands
# (x): An underload string:
# Starts with an opening parenthesis (, and pushes all characters after the starting ( and before the closing parenthesis ) as a string.
# Parentheses that come after the first ( must be matched, and a matched ) will not end the string.
# An Underload program can only contain balanced parentheses i.e. (() is an invalid program.
# If all parentheses in a string are not correctly matched, you must raise an Exception.
# :: Duplicate the top element of the stack.
# !: Remove the top element of the stack.
# ~: Swap the top two elements in the stack.
# *: Concatenate the top element of the stack to the end of the second element of the stack.
# The top element and second element are both popped and the concatenated string is pushed in their place.
# This is ordinary string concatenation, if the top of the stack is ["(a)","(b)"], the resulting stack should be ["(a)(b)"].
# a: Enclose the top element of the stack in a set of parentheses.
# ^: Include the top element of the stack into the program after this command. The top element is popped.
# The string must be inserted after the position of the ^ command being executed.
# For example, if the code is ^a* and the top of the stack is "S~!", then the code becomes ^S~!a*, and execution continues starting with S.
# S: Pop the top element of the stack, and output it (no newline). In the case of this challenge, you will have to store the output every time S is called, and return it as a single string at the end of the program.
# Code is interpreted from left to right.
#
# Invalid commands not mentioned in the command list must be ignored.
#
# Stack underflow is a condition where a command is run, but there are no arguments on the stack to use for it. You do not need to handle stack underflow.
#
# The program ends when it reaches the end of the code.
#
# You can learn more about Underload from its Esolangs Wiki page.


def underload(code):

    stack = []
    output = ''

    current_string = ''

    def duplicate():
        stack.append(stack[-1])

    def remove():
        stack.pop()

    def swap():
        stack[-2], stack[-1] = stack[-1], stack[-2]

    def concatenate():
        stack[-2] += stack[-1]
        stack.pop()

    def enclose():
        stack[-1] = '(' + stack[-1] + ')'

    def insert():
        insert_code = stack.pop()
        return insert_code

    def output_string():
        output += stack.pop()

    dispatch = {
        ':': duplicate,
        '!': remove,
        '~': swap,
        '*': concatenate,
        'a': enclose,
        '^': insert,
        'S': output_string
    }

    i = 0

    while i < len(code):
        if current_string:
            if code[i] == ")":
                stack.append(current_string)
                current_string = ""
            else:
                current_string += code[i]
        else:
            if code[i] == "(":
                current_string = ""
            elif code[i] in dispatch:
                insert_code = dispatch[code[i]]()
                if insert_code:
                    code = code[:i] + insert_code + code[i:]
            i += 1

    return output
