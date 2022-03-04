# Исключения. Exceptions

print('hello1')
print('hello2')
print('hello3')
try:
    int('hello')
except ValueError:
    print('ValueError')
print('hello4')
print('hello5')