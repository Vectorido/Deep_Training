def foo():
    return 14/0


try:
    foo()
except(ArithmeticError):
    print('ArithmeticError')
except(AssertionError):
    print('AssertionError')
except(ZeroDivisionError):
    print('ZeroDivisionError')
