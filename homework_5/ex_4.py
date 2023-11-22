integer = int(input())
# Start of with the assmution that the sum is 0
result = 0
# For each number from 1 to integer + 1 (because range takes out 1)
for number in range(1, integer + 1):
    # Increase result with its previous value and our next number
    result = result + number
print(result)
