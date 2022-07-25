from tabulate import tabulate


class Queue:

    def __init__(self):
        """
        Construct a queue (FIFO).
        """
        self.queue_list: list = []
        self.size = lambda: len(self.queue_list)  # Implement lambda on size to return the size of queue list

    def isEmpty(self):
        """
        If the size of queue list is 0
        """
        return len(self.queue_list) == 0

    def pop(self):
        """
        Dequeue the top item
        """
        return self.queue_list.pop(0) if not self.isEmpty() else None

    def append(self, item):
        """
        Append item into queue list
        """
        self.queue_list.append(item)

    def printQueue(self):
        """
        To print the items inside queue list
        """
        print(tabulate(self.queue_list, headers=['No.', 'DateTime', 'OrderId', 'Flavour', 'Weight', 'Price', 'Status'],
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
                    print('In Progress Summary', file=filename)
                    print(tabulate(self.queue_list,
                                   headers=['No.', 'DateTime', 'OrderId', 'Flavour', 'Weight', 'Price', 'Status'],
                                   showindex=True), file=filename)
                    print("Please check the summary report in Summary_report.txt. ")
                    filename.close()
                    break
                elif reply == 'no':
                    print("Ok. Have a nice day! ")
                    break
                else:
                    print("Invalid input! ")
            except:
                print("Invalid input! ")

