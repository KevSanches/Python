import sys
sum_numbers = 0

for line in sys.stdin:
    numbers = line.split()
    
for i in range(len(numbers)):
    sum_numbers += int(numbers[i])

print (sum_numbers)
