a = int(input('первое число = '))
b = int(input('второе число = '))
c = a * b
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(c / (a + b))
