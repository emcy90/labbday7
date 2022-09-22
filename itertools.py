"""
task about itertools
a. Please Check the documentation of itertools here then:
b. Create function string_perm_list(my_string) that return
list of all possible order of the input string “ABCD” so the
output like: (hint here)
['ABCD', 'ABDC', 'ACBD', 'ACDB',
'ADBC', 'ADCB', 'BACD', 'BADC'…]
c. Now create same function but it returns tuple
string_prem_tuple(my_string).
d. Use input_test_string= “0123456789” and check timing,
and memory_profile for both the list and tuple version.
e. What do think about results of both in d?
tuple-version:Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    29     20.0 MiB     20.0 MiB           1   @memory_profiler.profile
    30                                         def string_perm_tuple(my_string):
    31     20.0 MiB      0.0 MiB           1       nums = tuple(my_string)
    32    494.2 MiB    474.2 MiB           1       permutations = tuple(itertools.permutations(nums))
    33    744.1 MiB -11894.0 MiB     3628803       print([''.join(permutation) for permutation in permutations])


144.28652139997575
list-version:Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    30     20.1 MiB     20.1 MiB           1   @memory_profiler.profile
    31                                         def string_perm_list(my_string):
    32     20.1 MiB      0.0 MiB           1       nums = list(my_string)
    33     20.1 MiB      0.0 MiB           1       permutations = itertools.permutations(nums)
    34    494.3 MiB -133186.3 MiB     3628801       for i in list(permutations):
    35    494.3 MiB -133188.8 MiB     3628800           print(i)


721.5512715000659
"""
import timeit
import itertools
import memory_profiler


@memory_profiler.profile
def string_perm_list(my_string):
    nums = list(my_string)
    permutations = itertools.permutations(nums)
    for i in list(permutations):
        print(i)


#@memory_profiler.profile
def string_perm_tuple(my_string):
    nums = tuple(my_string)
    permutations = tuple(itertools.permutations(nums))
    print([''.join(permutation) for permutation in permutations])


def main():
    """main function to call on functions that uses itertools"""
    my_string = "ABCD"
    string_perm_list(my_string)
    string_perm_tuple(my_string)
    input_test_string = "0123456789"
    start_time_l_1 = timeit.default_timer()
    string_perm_list(input_test_string)
    print(timeit.default_timer() - start_time_l_1)

#    start_time_t_1 = timeit.default_timer()
#    string_perm_tuple(input_test_string)
#    print(timeit.default_timer() - start_time_t_1)


if __name__ == '__main__':
    main()
