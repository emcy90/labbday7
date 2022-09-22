"""
tuple vs list test which is faster and why:
when we look up info tuple is supposed to be faster but when we run our
functions list is faster until we go way higher in elements added. But
after several runs of it we do eventually get the simplest way to be slightly
faster for tuple over list (the create a tuple with 11 elements vs list with
11 elements)
According to one source:
List has a method called append() to add single items to the existing list.
So, for most of the append to be fast, python actually create a larger array in
memory every time you create a list — in case you append. Thus, making a list of
five elements will cost more than five elements worth of memory.
In contrary, since tuple is immutable, it asks for an immutable structure. This way
tuples are more explicit with memory.
Thus, making a tuple of five elements will cost only five elements worth of memory.
"""
import timeit


def tuple_test(n):
    """function to list a tuple of list"""
    tuple_1 = ()
    i = 0
    while i <= n:
        tuple_1 = tuple_1 + (i,)
        i += 1

    print(tuple_1)


def list_test(n):
    """function to list a list of numbers"""
    my_list = []
    i = 0

    while i <= n:
        my_list.append(i)
        i += 1

    print(my_list)


def main():
    """main function to print the tuples and lists"""
    start_time_t_1 = timeit.default_timer()
    tuple_test(10)
    print(timeit.default_timer() - start_time_t_1)

    start_time_l_1 = timeit.default_timer()
    list_test(10)
    print(timeit.default_timer() - start_time_l_1)

    start_time_t_2 = timeit.default_timer()
    tuple_1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(tuple_1)
    print(timeit.default_timer() - start_time_t_2)

    start_time_l_2 = timeit.default_timer()
    list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list_1)
    print(timeit.default_timer() - start_time_l_2)


if __name__ == '__main__':
    main()
