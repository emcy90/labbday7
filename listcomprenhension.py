"""
list comprehension
 List comprehension:
a. Using list comprehension create list av Fahrenheit from
this Celsius = [0,10,20.1,34.5]
b. Using Tuple comprehensive create tuple of T_Fahrenhite
from the same Celsius list in a.
c. Time both code and compare result , do the same using
memory_profile , what do u think?
[32.0, 50.0, 68.36, 94.1]
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    16     19.9 MiB     19.9 MiB           1   @memory_profiler.profile
    17                                         def convert_using_list(celsius):
    18     20.0 MiB      0.0 MiB           7       farenheit = [(temp * 9/5) + 32 for temp in celsius]
    19
    20     20.0 MiB      0.0 MiB           1       return print(farenheit)


0.06963589997030795
(32.0, 50.0, 68.36, 94.1)
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    22     20.0 MiB     20.0 MiB           1   @memory_profiler.profile
    23                                         def convert_using_tuples(celsius):
    24     20.0 MiB      0.0 MiB          11       farenheit = tuple((temp * 9/5) + 32 for temp in celsius)
    25     20.0 MiB      0.0 MiB           1       return print(farenheit)


0.002158000017516315

Process finished with exit code 0
tuples kicks lists butt. Clearly.
"""

import timeit

import memory_profiler

celsius = [0, 10, 20.2, 34.5]


@memory_profiler.profile
def convert_using_list(celsius):
    farenheit = [(temp * 9/5) + 32 for temp in celsius]

    return print(farenheit)

@memory_profiler.profile
def convert_using_tuples(celsius):
    farenheit = tuple((temp * 9/5) + 32 for temp in celsius)
    return print(farenheit)


start_time_list = timeit.default_timer()
convert_using_list(celsius)
print(timeit.default_timer() - start_time_list)

start_time_tup = timeit.default_timer()
convert_using_tuples(celsius)
print(timeit.default_timer() - start_time_tup)
