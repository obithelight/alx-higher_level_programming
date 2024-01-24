#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    mylist = []

    for item in range(list_length):
        try:
            answer = my_list_1[item] / my_list_2[item]

        except TypeError:
            print("wrong type")
            answer = 0
        except ZeroDivisionError:
            print("division by 0")
            answer = 0
        except IndexError:
            print("out of range")
            answer = 0
        finally:
            mylist.append(answer)

    return mylist
