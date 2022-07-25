from tabulate import tabulate # Import tabulate for printing report usage


class MinHeap:
    def __init__(self):
        """
        On this implementation the heap list is initialized with a value
        """
        self.heap_list: list = []
        self.current_size = lambda: len(self.heap_list)  # Implement lambda on current.size to return the size of heap
        # list

    def swap(self, i, j):
        """
        To define a function for swapping usage between two items, i and j
        """
        self.heap_list[i], self.heap_list[j] = self.heap_list[j], self.heap_list[i]

    def isEmpty(self):
        """
        If the size of the heap list is 0.
        """
        return len(self.heap_list) == 0

    def insert(self, item):
        """
        Inserts a value into the heap
        """
        self.heap_list.append(item)  # Append the item into the heap
        self.sift_up(self.current_size() - 1)  # To invoke siftup function, -1 to find the index of the inserted item,
        # which is known as recursive method

    def sift_up(self, i: int):
        """
        Sift up an item while heapify.
        """
        parent = lambda x: x // 2  # lambda implementation on parent index
        while i != 0 and self.heap_list[i] < self.heap_list[parent(i)]:  # If the inserted item has parent and smaller
            # than the parent
            self.swap(i, parent(i))  # Invoke the swapping function to swap between child and parent
            i = parent(i)  # To declared the swapped item become the parent as it is the smallest value.

    def sift_down(self, i: int):
        """
        Sift down an item while heapify.
        """
        leftChild = lambda x: x * 2  # lambda implementation on left child index
        rightChild = lambda x: (x * 2) + 1  # lambda implementation on right child index
        while True:  # To do it recursively
            j: int = i  # To initialize the smallest value to the parent
            if leftChild(j) < self.current_size() and self.heap_list[leftChild(j)] < self.heap_list[i]:
                i = leftChild(j)  # To check if left child exist
                # If exist and left child is smaller than parent, the smallest value is left child
            if rightChild(j) < self.current_size() and self.heap_list[rightChild(j)] < self.heap_list[i]:
                i = rightChild(j)  # To check if left child exist
                # If exist and left child is smaller than parent or left child, the smallest value is right child
            if i != j:  # Check if the smallest value is not equal to the index
                self.swap(i, j)  # Swap to the correct position
            else:
                break

    def delete_min(self):
        """
        Remove and return the item on the top of the heap.
        """
        if not self.isEmpty():
            self.swap(0, self.current_size() - 1)  # Swap the first node with the last node
            pop = self.heap_list.pop(self.current_size() - 1)  # Keep the last node, which is the smallest value
            # after swapping in variable pop
            self.sift_down(0)  # When invoke siftdown function will always start at the root
            return pop

    def printHeap(self):
        """
        To print the items inside heap list
        """
        print(tabulate(self.heap_list,
                       headers=['No.', 'DateTime', 'OrderId', 'Flavour', 'Weight', 'Price', 'Status'],
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
                    print("Outstanding Summary", file=filename)
                    print(tabulate(self.heap_list,
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
