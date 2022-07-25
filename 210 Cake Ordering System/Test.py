class Stack(object):
    """ uses an array to implement a stack """

    def __init__(self):
        self.data = []

    def push(self, num):
        """Push stack operation """
        self.data.append(num)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def __len__(self):
        return len(self.data)

    def isEmpty(self):
        return True if len(self.data) == 0 else False

    def clear(self):
        self.data = []

    def __repr__(self):
        return 'Stack_' + str(self.data)

    def __str__(self):
        return 'Stack_' + str(self.data)


def isBalance(text):
    result_stack = Stack()
    for i in text:
        if i in ['{', '[', '(']:
            result_stack.push(i)
        elif i in ['}', ']', ')']:
            # encounter end brackets
            if result_stack.isEmpty():
                # If the current stack is empty, does not match, returns False
                return False
            chFromStack = result_stack.pop()

            if not ((chFromStack == '{' and i == '}')
                    or (chFromStack == '[' and i == ']')
                    or (chFromStack == '(' and i == ')')):
                return False
            return True
    return result_stack.isEmpty()

