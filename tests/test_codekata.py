from codekata.codekata import yeh, fizzbuzz

def test_yeh():
    assert yeh() == 'yeh'


def test_fizzbuzz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"
    assert fizzbuzz(45) == "FizzBuzz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(1) == 1
