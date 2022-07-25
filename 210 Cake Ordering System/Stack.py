from tabulate import tabulate


class Stack:

    def __init__(self):
        self.stack_list: list = []
        self.size = lambda: len(self.stack_list)  # Implement lambda on size to return the size of queue list
        self.itemList: list = []

    def isEmpty(self):
        """
        If the size of stack list is 0
        """
        return len(self.stack_list) == 0

    def push(self, item):
        """
        Append item into stack list
        """
        self.stack_list.append(item)

    def pop(self):
        """
        Pop item out from stack list
        """
        return self.stack_list.pop() if not self.isEmpty() else None

    def printStack(self, n):
        """
        To print the items inside stack list
        """
        stack = reversed(self.stack_list)
        for item in stack:
            if n != 0:
                self.itemList.append(item)
                n -= 1
        print(tabulate(self.itemList, headers=['No.', 'DateTime', 'OrderId', 'Flavour', 'Weight', 'Price', 'Status'],
                       tablefmt='fancy_grid', showindex=True))

    def printreport(self):
        """
        To print the report into another file as text file
        """
        while True:
            try:
                reply = str(input("Do you want to print the summary report? (Yes / No): ")).lower()
                if reply == 'yes':
                    filename = open('Summary_report.txt', 'w')
                    print('Delivered Summary', file=filename)
                    print(tabulate(self.itemList,
                                   headers=['No.', 'DateTime', 'OrderId', 'Flavour', 'Weight', 'Price', 'Status'],
                                   showindex=True), file=filename)
                    print("Please check the summary report in Summary_report.txt. ")
                    filename.close()
                    self.itemList.clear()
                    break
                elif reply == 'no':
                    print("Ok. Have a nice day! ")
                    break
                else:
                    print("Invalid input! ")
            except:
                print("Invalid input! ")
