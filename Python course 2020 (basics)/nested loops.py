#nested loops
numbers = [5, 2, 5, 2, 2, 12, 28, 4]

for number in numbers:
    output = ''
    for count in range(number):
        output += 'x'
    print(output)
