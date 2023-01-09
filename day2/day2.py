
with open(r"src\advent_of_code2022\day2\day2.txt", "r") as f: # 14610
    numbers = f.read()

number = numbers.split("\n")
#print(number)

def day2_task1(s: str) -> int:

    table = {"A X":4, "A Y":8, "A Z":3, "B X":1, "B Y":5, "B Z":9,"C X":7, "C Y":2, "C Z":6}
    # table = {"A X":3, "A Y":4, "A Z":8, "B X":1, "B Y":5, "B Z":9,"C X":2, "C Y":6, "C Z":7}
    total = 0
    for i in s:
        #print(i)
        total += table[i]

    return total

def day2_task2(s: str) -> int:

    # table = {"A X":4, "A Y":8, "A Z":3, "B X":1, "B Y":5, "B Z":9,"C X":7, "C Y":2, "C Z":6}
    table = {"A X":3, "A Y":4, "A Z":8, "B X":1, "B Y":5, "B Z":9,"C X":2, "C Y":6, "C Z":7}
    total = 0
    for i in s:
        #print(i)
        total += table[i]

    return total

result = day2_task1(number) # *********** correct ****************
print("advent of code 2022 day 2 task 1: ", result)

result = day2_task2(number)  # *********** correct ****************
print("advent of code 2022 day 2 task 2: ", result)
    
    