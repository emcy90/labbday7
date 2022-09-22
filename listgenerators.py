"""Task to do in this file:
List Generators:
a. Create a function power2(n) that return list of power
2(like 3**2) of list from 0-(n-1)?
b. Then create a function power2_generator(n) that do the
same thing as power2(n) but as generator! Hint here
c. Write needed code to print the list elements in both
cases!
d. Check timeit and memory profile for both functions
power2(n) and power2_generator(n) for n=10000.
"""
import timeit
import memory_profiler


@memory_profiler.profile
def power_2(n):
    """function for power of 2"""
    i = 0
    my_list = []
    while i < n:
        power = i ** 2
        my_list.append(power)
        i += 1
    print(my_list)


@memory_profiler.profile
def power_2_generator(n):
    """generator for power of 2"""
    i = 0
    while i < n:
        yield i ** 2
        i += 1


def main():
    """main function to test list generator"""
    start_time_pow = timeit.default_timer()
    power_2(10000)
    print(timeit.default_timer() - start_time_pow)

    start_time_gen = timeit.default_timer()
    result = []
    for num in power_2_generator(10000):
        result.append(num)
    print(result)
    print(timeit.default_timer() - start_time_gen)


if __name__ == '__main__':
    main()

