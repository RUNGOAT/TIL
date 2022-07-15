numbers = [34, 56, 23, 34, 12]
total1 = 0
total2 = 0
for number in numbers :
    total1 += number
print(total1)

print()

for i in range(len(numbers)) :
    total2 += numbers[i]
print(total2)

