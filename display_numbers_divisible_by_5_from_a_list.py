# Assignment 5 - Exercise 6
# Iterate the given list of numbers and print only those numbers which are divisible by 5

# Request input for list from user

number_list = [int(input("First Number: ")), int(input("Second Number: ")), int(input("Third Number: ")), int(input("Fourth Number: ")), int(input("Fifth Number: "))]

# Print the list

print("\nGiven List:", number_list)

# Print numbers that are divisible by 5

print("\nNumbers divisible by 5: ")

for number in number_list:
    if number % 5 == 0:
        print(number)