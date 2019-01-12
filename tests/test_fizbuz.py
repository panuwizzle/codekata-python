from codekata.fizbuz import fizbuz

def test_fizbuz():
    assert fizbuz(3) == 'Fizz'
    assert fizbuz(5) == 'Buzz'
    assert fizbuz(1) == 1
    assert fizbuz(2) == 2
    assert fizbuz(15) == 'FizzBuzz'
    assert fizbuz(30) == 'FizzBuzz'
