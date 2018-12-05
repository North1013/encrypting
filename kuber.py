n = int(input("n?\n"))

test = 0
calc = []

for i in range(n + 1):
    calc.append(i*i*i)

for i in calc:
    test += i

print(test)
