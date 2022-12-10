from AdventOfCode import AdventOfCode


# this class is used to create instance of the other classes (to "drive" the different programs)
class DriverClass:

    adventOfCode = AdventOfCode()
    adventOfCode.introduction()

    # Open the file in reading mode
    with open("Day1.txt", "r") as f:
        # Read the contents of the file
        numbers = f.read()
        # Split the contents of the file into a list of strings
        numbers = numbers.split('\n')

    # Call the biggest_item() function with the contents of the file as the argument

    #result = adventOfCode.biggest_item(numbers)
    #print("advent of code 2022 day 1 task 1: biggest item is", result)

    result = adventOfCode.biggest_3_items(numbers)
    print("advent of code 2022 day 1 task 2: biggest item is", result)