'''
a. Using list comprehensive create list av Fahrenheit from
this Celsius = [0,10,20.1,34.5]
b. Using Tuple comprehensive create tuple of T_Fahrenhite
from the same Celsius list in a.
c. Time both code and compare result , do the same using
memory_profile , what do u think?
'''


celsius = [0, 10, 20.2, 34.5]


def using_list(celsius):
    farenheit = [(temp * 9/5) + 32 for temp in celsius]

    return print(farenheit)


using_list(celsius)
