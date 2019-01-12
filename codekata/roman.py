def dec_to_roman(dec):
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    result = []

    """ loop through the tuble """
    for i in range(len(ints)):
        """ count the number of each base """
        count = int(dec / ints[i])
        """ append the base to the list """
        result.append(nums[i] * count)
        """ minus the input down for the next base """
        dec -= ints[i] * count
    return ''.join(result)
