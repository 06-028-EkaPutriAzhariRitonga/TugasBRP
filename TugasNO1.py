height = int(input("Input height segitiga: "))

for i in range(height):
    print(" " * (height - i - 1) + '*' * (i * 2 + 1))