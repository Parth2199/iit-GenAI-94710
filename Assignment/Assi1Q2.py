nums = input("Enter numbers (comma-separated): ")

# Convert input string → list of integers
numbers = [int(x.strip()) for x in nums.split(",")]

even_count = 0
odd_count = 0

for n in numbers:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
