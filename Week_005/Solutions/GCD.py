import math

def gcd_of_list(numbers):
    result = numbers[0]   # start with the first number
    for i in range(1, len(numbers)):
        result = math.gcd(result, numbers[i])  # update gcd
        if result == 1:   # optimization: gcd can’t be less than 1
            return 1
    return result

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(gcd_of_list(arr))
