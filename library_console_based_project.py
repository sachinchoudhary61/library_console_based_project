LB = ['mathematics', 'science', 'English']
LM = ['sachu', 'pee-nut', 'Kas-vo']


class AM:
    def __init__(self):
        mem_num = int(input("Enter the number of member you want to add : "))
        print("Enter the name of the member : ")
        for i in range(mem_num):
            mem_name = input()
            LM.append(mem_name)
        print("MEMBER ADDED SUCCESFULLY ")


class AB:
    def __init__(self):
        book_num = int(input("Enter the number of book you want to add : "))
        print("Enter the name of the book : ")
        for i in range(book_num):
            book_name = input()
            LB.append(book_name)
        print("BOOK ADDED SUCCESFULLY ")


class BB:
    def __init__(self):
        book_num2 = int(input("Enter the number of book you would like to borrow from the library ?: "))

        if book_num2 < 3:
            print("Enter the names of the book you would like to borrow from the library ?:  ")
            for i in range(book_num2):
                book_name2 = input()
                LB.remove(book_name2)
                print("BOOK IS ISSUED")
                print("AVAILABLE BOOKS : ", LB)
        else:
            print("SORRY::( , you cannot borrow more than two books")


class RB:
    def __init__(self):
        book_num3 = int(input("Enter the number of book you would like to return ? : "))
        print("Enter the name of the books ?: ")
        for i in range(book_num3):
            book_name = input()

            LB.extend(book_name)

        print("NOW, You have returned a book sucessfully")


class VMS:
    def __init__(self):
        print("Enter the name of the member : ")
        mem_name = input()
        count = 0
        for i in LM:
            if mem_name == i:
                count = count + 1
        if (count > 0):
            print("YOU ARE THE MEMBER OF THE LIBRARY")

        else:
            print("SORRY :(,YOU ARE NOT THE MEMBER OF THE LIBRARY")

            print("DO YOU WANT TO GET THE MEMBERSHIP : YES=1/NO=0")
            check = int(input())
            if (check == 1):
                AM()
            else:
                print("AS YOU WISH")


class BS:
    def __init__(self):
        print("Enter the name of the book : ")
        book_name4 = input()
        count = 0
        for i in LB:
            if book_name4 == i:
                count = count + 1

        if (count > 0):
            print("BOOK IS CURRENTLY PRESENT IN THE LIBRARY")
        else:
            print("SORRY :(,CURRENTLY BOOK IS NOT AVAILABLE")


print("\n ==========*==*==UNIVERSITY INSTITUTE OF INFORMATION TECHNOLOGY, HPU-SHIMLA==*==*===========\n"
      "                       ====*==*==WELCOME TO THE LIBRARY==*==*====\n"
      "1.Add new member \n"
      "2.Add new book\n"
      "3.Borrowing process\n"
      "4.Returning process\n"
      "5.View member status\n"
      "6.view Book status\n"
      "7.Quit\n"
      "==================================================================================\n")

while True:
    choice = int(input("Enter choice : "))

    if choice == 1:
        AM()
    elif choice == 2:
        AB()
    elif choice == 3:
        BB()
    elif choice == 4:
        RB()
    elif choice == 5:
        VMS()
    elif choice == 6:
        BS()
    elif choice == 7:
        print(" :)*===*THANK YOU, HOPE YOU COME BACK*===* :) ")
        break
