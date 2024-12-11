import random
def generate_random_numbers(n, start, end):
    if start > end:
        print("Start of the range must be less than or equal to the end.")
        return 0
    if n < 0:
        print("Number of random numbers (n) must be non-negative.")
        return 0

    random_numbers = list()
    for i in range(n):
        random_numbers.append(random.randint(start, end))
    
    return random_numbers

n = int(input("Enter the number of random numbers to generate: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

random_numbers = generate_random_numbers(n, start, end)
if random_numbers != 0:
    for i in range(n):
        print(random_numbers[i], end=" ")