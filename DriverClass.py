from AdventOfCode import AdventOfCode


# this class is used to create instance of the other classes (to "drive" the different programs)
class DriverClass:

    adventOfCode = AdventOfCode()
    adventOfCode.introduction()

    # ********************************** DAY 1 *******************************************

    # Open the file in reading mode
    with open("Day1.txt", "r") as f:

        # Read the contents of the file
        numbers = f.read()

        # Split the contents of the file into a list of strings
        numbers = numbers.split('\n')

    result = adventOfCode.day1_task1(numbers) # *********** correct ****************
    print("advent of code 2022 day 1 task 1: biggest item is", result)

    result = adventOfCode.day1_task2(numbers) # *********** correct ****************
    print("advent of code 2022 day 1 task 2: biggest item is", result)

    # ********************************** DAY 2 *******************************************

    with open("Day2.txt", "r") as f: # 14610
        numbers = f.read()

    number = numbers.split("\n")
    #print(number)

    #result = adventOfCode.total_score(number) *********** FAIL *******************
    result = adventOfCode.day2_task1(number) # *********** correct ****************
    print("advent of code 2022 day 2 task 1: ", result)

    result = adventOfCode.day2_task2(number)  # *********** correct ****************
    print("advent of code 2022 day 2 task 2: ", result)