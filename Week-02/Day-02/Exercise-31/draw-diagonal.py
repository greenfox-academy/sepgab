a = int(input("Give me a number for the diagonal: "))
sq = '%'
space = ' '
print(sq * a)
for i in range(0, a - 2):
    print(sq + space * i + sq + space * (a - i - 3) + sq)
print(sq * a)
