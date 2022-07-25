import datetime
import time

from Heap import MinHeap
from Queue import Queue
from Stack import Stack


if __name__ == '__main__':
    a = MinHeap()
    b = Queue()
    c = Stack()
    count = 0

    print('------------------------------ Cake Ordering System --------------------------------')
    main_menu = (
        'Add a new order',
        'Retrieve an order',
        'Deliver an order',
        'Print summary report',
        'Exit system')

    summary = (
        'Outstanding order list',
        'Work In progress',
        'Top n latest order delivered')

    while True:
        for i in range(len(main_menu)):
            print('{}) {}'.format(i + 1, main_menu[i]))
        try:
            com = int(input('\nChoose an option: '))
            if com > 5 or com < 1:
                print('Incorrect input!\n')
                print('------------------------------------------------------------------------------------\n')
        except ValueError:
            print('Incorrect input!\n')
            print('------------------------------------------------------------------------------------\n')
            continue
        if com == 5:
            print('Thank you!')
            break
        elif com == 1:
            orderdetail = []

            count += 1
            if count > 0:
                id = '{:d}'.format(count).zfill(4)
                print('Order ID: ' + id)
                orderdetail.append(id)

            while True:
                try:
                    date = str(input("Please enter the date in dd/mm/yyyy format: "))
                    x = date.split('/')
                    if int(x[1]) < 10:
                        x[1] = '0' + x[1]

                    if int(x[0]) < 10:
                        x[0] = '0' + x[0]

                    while len(x) != 3:
                        try:
                            print("Invalid input!")
                            date = str(input("Please enter the date in dd/mm/yyyy format: "))
                            x = date.split('/')
                        except None:
                            pass

                    while True:
                        try:
                            datetime.datetime(int(x[2]), 1, 1)
                            break
                        except ValueError or IndexError or len(x) != 3:
                            print("Invalid input for year.")
                            x[2] = str(input("Please enter the year again: "))

                    while True:
                        try:
                            datetime.datetime(int(x[2]), int(x[1]), 1)
                            break
                        except ValueError or IndexError:
                            print("Invalid input for month.")
                            x[1] = str(input("Please enter the month again: "))

                    while True:
                        try:
                            datetime.datetime(int(x[2]), int(x[1]), int(x[0]))
                            break
                        except ValueError or IndexError:
                            print("Invalid input for day.")
                            x[0] = str(input("Please enter the day again: "))
                    break

                except IndexError:
                    print("Invalid input! ")

            while True:
                try:
                    hours = str(input("Please enter the time in 24 hours and hh:mm format: "))
                    y = hours.split(':')

                    if int(y[0]) < 10:
                        y[0] = '0' + y[0]

                    while len(y) != 2:
                        try:
                            print("Invalid input!")
                            hours = str(input("Please enter the time in 24 hours and hh:mm format: "))
                            y = hours.split(':')
                        except None:
                            pass

                    while True:
                        try:
                            datetime.datetime(2021, 1, 1, int(y[0]))
                            break
                        except ValueError or IndexError:
                            print("Invalid input for hour.")
                            y[0] = str(input("Please enter hour again: "))

                    while True:
                        try:
                            datetime.datetime(2021, 1, 1, 12, int(y[1]))
                            break
                        except ValueError or IndexError:
                            print("Invalid input for minute.")
                            y[1] = str(input("Please enter the minute again: "))

                    temp = x[2]
                    x[2] = x[0]
                    x[0] = temp
                    Date = x + y
                    date_min_heap = ''.join(Date)
                    orderdetail.append(date_min_heap)
                    break

                except IndexError and ValueError:
                    print("Invalid input! ")

            while True:
                try:
                    cake = str(
                        input("Name of cake(Flavour:[Cheese Cake, Black Forest, Tiramisu, Fruit Cake]): ")).lower()
                    if cake == "cheese cake" or cake == "black forest" or cake == "tiramisu" or cake == "fruit cake":
                        orderdetail.append(cake)
                        break
                    else:
                        print("Invalid input. Only the 4 options are available")
                except:
                    print("Invalid input. Only the 4 options are available")

            while True:
                try:
                    weight = str(input("Weight of cake (0.5kg, 1kg, 2kg): "))
                    weight = float((weight.replace("kg", "")))
                    if weight == 0.5:
                        x = str(weight) + 'kg'
                        price = "RM30"
                        orderdetail.append(x)
                        orderdetail.append(price)
                        break
                    elif weight == 1:
                        x = str(weight) + 'kg'
                        price = "RM60"
                        orderdetail.append(x)
                        orderdetail.append(price)
                        break
                    elif weight == 2:
                        x = str(weight) + 'kg'
                        price = "RM90"
                        orderdetail.append(x)
                        orderdetail.append(price)
                        break
                    else:
                        print("Only 3 choices of weights are available. Please try again")

                except:
                    print("Only 3 choices of weights are available. Please try again")

            status = "NEW"
            orderdetail.append(status)

            changepos = orderdetail[1]
            orderdetail[1] = orderdetail[0]
            orderdetail[0] = changepos

            a.insert(orderdetail)
            print(orderdetail)

            print('Adding......')
            time.sleep(1)
            print('Order added successfully.\n')
            print('------------------------------------------------------------------------------------\n')
            time.sleep(0.5)

        elif com == 2:
            if not a.isEmpty():
                retrieveorder = a.delete_min()
                retrieveorder[5] = 'In Progress'
                b.append(retrieveorder)
                print('Retrieving......')
                time.sleep(1)
                print('Order retrieved successfully.\n')
                print('------------------------------------------------------------------------------------\n')
                time.sleep(0.5)

            else:
                print('Please add an order before retrieving!\n')
                print('------------------------------------------------------------------------------------\n')

        elif com == 3:
            if not b.isEmpty():
                deliverorder = b.pop()
                deliverorder[5] = 'Delivered'
                c.push(deliverorder)
                print('Delivering......')
                time.sleep(1)
                print('Order delivered successfully.\n')
                print('------------------------------------------------------------------------------------\n')
                time.sleep(0.5)
            else:
                print('Please add an order and retrieve it before delivering!\n')
                print('------------------------------------------------------------------------------------\n')

        elif com == 4:
            try:
                print('\nWhich report would you like to view:')
                for i in range(len(summary)):
                    print('{}) {}'.format(i + 1, summary[i]))

                num = int(input('Enter: '))
                if num == 1:
                    if not a.isEmpty():
                        print('Generating......\n')
                        time.sleep(1)
                        a.printHeap()
                        a.printreport()
                        print('------------------------------------------------------------------------------------\n')
                        time.sleep(0.5)

                    else:
                        print('There are no outstanding orders!\n')
                        print('------------------------------------------------------------------------------------\n')

                elif num == 2:
                    if not b.isEmpty():
                        print('Generating......\n')
                        time.sleep(1)
                        b.printQueue()
                        b.printreport()
                        print('------------------------------------------------------------------------------------\n')
                        time.sleep(0.5)

                    else:
                        print('There are no work in progress orders!\n')
                        print('------------------------------------------------------------------------------------\n')

                elif num == 3:
                    if not c.isEmpty():
                        c.printStack(int(input('n: ')))
                        c.printreport()
                        print('------------------------------------------------------------------------------------\n')
                    else:
                        print('There are no latest orders!\n')
                        print('------------------------------------------------------------------------------------\n')
                else:
                    print('Incorrect input!\n')
                    print('------------------------------------------------------------------------------------\n')

            except ValueError:
                print('Incorrect input!\n')
                print('------------------------------------------------------------------------------------\n')
