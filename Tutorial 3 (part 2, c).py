x = float(input('Give me a number: '))
fraction = x - int(x)
print(x,fraction)
if fraction > 0:
    print(x, "something else ")
elif int(x)%2 > 0:
    print(x, 'Odd')
else:
    print("Even")
