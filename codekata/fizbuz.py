def fizbuz(x):
    v = ''
    if x % 3 == 0 and x % 5 == 0:
        v = 'FizzBuzz'
    elif x % 3 == 0:
        v = 'Fizz'
    elif x % 5 == 0:
        v = 'Buzz'
    else:
        v = x
    return v
