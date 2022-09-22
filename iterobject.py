"""
iter object problem
a. Converting data types like string to iter object is very
useful. Read documentation about iter() and next() here
and then answer these questions:
b. Let’s say my_string = “I’m not iterator object” try
command next(my_string) what you get?
c. Create function that convert a string to iterator and print
each character in single line using next().
"""

def iterobject_version_1(val):
    """converting object to iterable using dunder-function"""
    data = val.__iter__()

    while True:
        try:
            print(data.__next__())
        except:
            break


def iterobject_version_2(val):
    data = iter(val)
    while True:
        try:
            print(next(data))
        except:
            break


def main():
    """main function to call on functions to run iteration of object"""
    my_string = "I’m not iterator object"
    #print(next(my_string))
    #next prints out str object is not an iterator
    #iterobject_version_1(my_string)
    iterobject_version_2(my_string)


if __name__ == '__main__':
    main()
